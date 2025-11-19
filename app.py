"""Modern Content Generator Web App using LangExtract."""

import os
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import json
import io
import sys
from pathlib import Path

# Add parent directory to path to import langextract
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

import langextract as lx

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'langextract-content-generator-2025')

# Configuration
UPLOAD_FOLDER = 'temp_uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    """Main page."""
    return render_template('index.html')


@app.route('/api/extract', methods=['POST'])
def extract_content():
    """Extract content from text using LangExtract."""
    try:
        data = request.get_json()
        
        text = data.get('text', '').strip()
        prompt = data.get('prompt', '').strip()
        api_key = data.get('api_key', '').strip()
        model_id = data.get('model_id', 'gemini-2.0-flash-exp')
        
        # Validation
        if not text:
            return jsonify({
                'success': False,
                'error': 'Please provide text to analyze.'
            })
        
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'Please provide extraction instructions.'
            })
        
        if not api_key:
            # Try to get from environment
            api_key = os.environ.get('LANGEXTRACT_API_KEY')
            if not api_key:
                return jsonify({
                    'success': False,
                    'error': 'Please provide a Gemini API key or set LANGEXTRACT_API_KEY environment variable.'
                })
        
        # Parse examples if provided, otherwise create default example
        examples = []
        if 'examples' in data and data['examples']:
            for ex in data['examples']:
                extractions = [
                    lx.data.Extraction(
                        extraction_class=e['class'],
                        extraction_text=e['text'],
                        attributes=e.get('attributes', {})
                    )
                    for e in ex.get('extractions', [])
                ]
                examples.append(lx.data.ExampleData(
                    text=ex['text'],
                    extractions=extractions
                ))
        
        # If no examples provided, create a generic example based on the prompt
        if not examples:
            # Create a simple example to guide the model
            examples = [
                lx.data.ExampleData(
                    text="This is a sample sentence with important content.",
                    extractions=[
                        lx.data.Extraction(
                            extraction_class="example_class",
                            extraction_text="important content",
                            attributes={"note": "This is an example"}
                        )
                    ]
                )
            ]
        
        # Perform extraction
        result = lx.extract(
            text_or_documents=text,
            prompt_description=prompt,
            examples=examples,
            model_id=model_id,
            api_key=api_key
        )
        
        # Format results
        extractions_data = []
        if result.extractions:
            for ext in result.extractions:
                ext_dict = {
                    'class': ext.extraction_class,
                    'text': ext.extraction_text,
                    'attributes': ext.attributes if hasattr(ext, 'attributes') else {}
                }
                # Only add start_char and end_char if they exist
                if hasattr(ext, 'start_char'):
                    ext_dict['start_char'] = ext.start_char
                if hasattr(ext, 'end_char'):
                    ext_dict['end_char'] = ext.end_char
                extractions_data.append(ext_dict)
        
        return jsonify({
            'success': True,
            'extractions': extractions_data,
            'count': len(extractions_data),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Extraction failed: {str(e)}'
        })


@app.route('/api/export/<format>', methods=['POST'])
def export_results(format):
    """Export results in various formats."""
    try:
        data = request.get_json()
        extractions = data.get('extractions', [])
        text = data.get('text', '')
        
        if format == 'json':
            output = json.dumps({
                'text': text,
                'extractions': extractions,
                'exported_at': datetime.now().isoformat()
            }, indent=2, ensure_ascii=False)
            
            return jsonify({
                'success': True,
                'content': output,
                'filename': f'extractions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            })
        
        elif format == 'html':
            html = generate_html_report(text, extractions)
            return jsonify({
                'success': True,
                'content': html,
                'filename': f'report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
            })
        
        elif format == 'csv':
            csv_content = generate_csv(extractions)
            return jsonify({
                'success': True,
                'content': csv_content,
                'filename': f'extractions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            })
        
        else:
            return jsonify({
                'success': False,
                'error': f'Unsupported format: {format}'
            })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Export failed: {str(e)}'
        })


def generate_html_report(text, extractions):
    """Generate HTML report from extractions."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extraction Report - {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        h1 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        .meta {{
            color: #666;
            margin-bottom: 30px;
        }}
        .text-section {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 4px solid #667eea;
        }}
        .extraction {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 4px solid #f093fb;
        }}
        .extraction-class {{
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 10px;
        }}
        .extraction-text {{
            font-size: 16px;
            color: #2d3748;
            margin: 10px 0;
            font-style: italic;
        }}
        .attributes {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }}
        .attribute {{
            background: #f0f4f8;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 14px;
        }}
        .attribute-key {{
            font-weight: bold;
            color: #4a5568;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 32px;
            font-weight: bold;
            display: block;
        }}
        .stat-label {{
            font-size: 14px;
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Extraction Report</h1>
        <div class="meta">Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        
        <div class="stats">
            <div class="stat-card">
                <span class="stat-number">{len(extractions)}</span>
                <span class="stat-label">Total Extractions</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{len(set(e['class'] for e in extractions))}</span>
                <span class="stat-label">Unique Classes</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{len(text)}</span>
                <span class="stat-label">Characters</span>
            </div>
        </div>
        
        <h2>📝 Original Text</h2>
        <div class="text-section">{text}</div>
        
        <h2>🔍 Extractions</h2>
"""
    
    for i, ext in enumerate(extractions, 1):
        html += f"""
        <div class="extraction">
            <span class="extraction-class">{ext['class']}</span>
            <div class="extraction-text">"{ext['text']}"</div>
"""
        if ext.get('attributes'):
            html += '<div class="attributes">'
            for key, value in ext['attributes'].items():
                html += f'<div class="attribute"><span class="attribute-key">{key}:</span> {value}</div>'
            html += '</div>'
        
        html += '</div>'
    
    html += """
    </div>
</body>
</html>"""
    
    return html


def generate_csv(extractions):
    """Generate CSV from extractions."""
    import csv
    from io import StringIO
    
    output = StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(['Class', 'Text', 'Start', 'End', 'Attributes'])
    
    # Data
    for ext in extractions:
        attrs = json.dumps(ext.get('attributes', {}))
        writer.writerow([
            ext['class'],
            ext['text'],
            ext.get('start_char', ''),
            ext.get('end_char', ''),
            attrs
        ])
    
    return output.getvalue()


@app.errorhandler(413)
def too_large(e):
    """Handle file too large error."""
    return jsonify({
        'success': False,
        'error': 'File is too large. Maximum size is 16MB.'
    }), 413


@app.errorhandler(500)
def internal_error(e):
    """Handle internal server error."""
    return jsonify({
        'success': False,
        'error': 'Internal server error. Please try again later.'
    }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
