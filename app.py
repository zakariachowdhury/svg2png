from flask import Flask, request, send_file
import cairosvg
import os
import io

app = Flask(__name)

@app.route('/convert', methods=['POST'])
def convert_svg_to_png():
    try:
        # Check if the request contains a file
        if 'file' not in request.files:
            return "No file provided", 400

        # Get the uploaded SVG file
        svg_file = request.files['file']

        # Ensure the file is an SVG
        if not svg_file.filename.endswith('.svg'):
            return "File must be in SVG format", 400

        # Get the original file name without the extension
        original_filename = os.path.splitext(svg_file.filename)[0]

        # Convert the SVG to a PNG in-memory
        png_data = cairosvg.svg2png(bytestring=svg_file.read())

        # Return the PNG as a response with the original file name
        return send_file(
            io.BytesIO(png_data),
            mimetype='image/png',
            as_attachment=True,
            download_name=f'{original_filename}.png'
        )
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
