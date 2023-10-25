SVG to PNG Converter API

This is a simple Flask API that converts SVG files to PNG format. You can use this API to convert SVG images into PNG images.

Getting Started

Follow these instructions to set up and run the API locally.

Prerequisites

- Python 3
- pip

Installation

1. Clone the repository:

   git clone https://github.com/zakariachowdhury/svg2png.git
   cd svg2png

2. Create a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the required packages:

   pip install -r requirements.txt

Usage

1. Start the Flask API:

   python app.py

2. The API will be running locally at http://localhost:5000.

3. To convert an SVG file to a PNG, make a POST request to http://localhost:5000/convert. You can use tools like cURL or Postman, or write your own script.

API Endpoint

- POST /convert: Upload an SVG file and get a converted PNG file in response.

Example

Here's an example of using cURL to convert an SVG file:

curl -F "file=@yourfile.svg" http://localhost:5000/convert --output converted.png

Contributing

Feel free to contribute to this project. You can fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

- Flask: https://flask.palletsprojects.com/
- CairoSVG: https://cairosvg.readthedocs.io/

Happy coding!
