from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_background():
    file = request.files['image']
    input_bytes = file.read()
    output_bytes = remove(input_bytes)
    
    output_img = Image.open(io.BytesIO(output_bytes))
    img_io = io.BytesIO()
    output_img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='no-bg.png')

if __name__ == '__main__':
    app.run(debug=True)
