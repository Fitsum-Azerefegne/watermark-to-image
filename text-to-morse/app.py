from flask import Flask, render_template, request

app = Flask(__name__)

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)

@app.route('/', methods=['GET'])
def home():
    return render_template('morse_code_convertor.html')

@app.route('/convert', methods=['POST'])
def convert():
    user_input = request.form['textInput']
    morse_output = text_to_morse(user_input)
    return render_template('morse_code_convertor.html', morse_code=morse_output)

if __name__ == '__main__':
    app.run(debug=True)