import subprocess
import os
from flask import Flask, request, render_template
import sys
 
app = Flask(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    test_output = None
    filename = None
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return render_template('upload.html', test_output=test_output)
        test_script = request.form['test_script']  # Get selected test script
        filename = file.filename
        new_filename=''

        if test_script == 'test_grader.py':
            new_filename="grader.py"
        elif test_script == 'test_bank_account.py':
            new_filename="bank_account.py"
        else:
            new_filename="seat_reservation.py"
        # new_filename += os.path.splitext(file.filename)[1]

        upload_dir = os.path.join(app.root_path, './upload')
        print("os path="+ str(os.path.abspath(upload_dir)))

        filepath = os.path.join(upload_dir, new_filename)
        file.save(filepath)

        # Execute test script
        test_script_path = f'./{test_script}'
        test_script_path = os.path.join(app.root_path, f'./tests/{test_script}')
        print ("test_script_path="+test_script_path)
        result = subprocess.run(['python', '-m', 'unittest', test_script_path], capture_output=True, text=True)
        print(result.stdout)
        
        test_output = result.stdout + result.stderr

    return render_template('upload.html', test_output=test_output, filename=filename)

if __name__ == '__main__':
    app.run(debug=False)
