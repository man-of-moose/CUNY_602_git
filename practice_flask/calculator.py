from flask import Flask, request, render_template
import re

app = Flask(__name__)


# main_page = '''
# <html>
#     <head>
#     <title></title>
#     <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
#     <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
#     </head>
# <body>
# <form class="form-horizontal" method="post" action="/calc">
# <fieldset>
# <!-- Form Name -->
# <legend>Multiplier</legend>
# <!-- Text input-->
# <div class="form-group">
#   <label class="col-md-4 control-label" for="textinput">Number</label>
#   <div class="col-md-4">
#   <input id="textinput" type="number" placeholder="Enter a number" class="form-control input-md">
#   </div>
# </div>
# <!-- Button -->
# <div class="form-group">
#   <label class="col-md-4 control-label" for="singlebutton"></label>
#   <div class="col-md-4">
#     <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
#   </div>
# </div>
# </fieldset>
# </form>
# <script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
# </body>
# </html>
# '''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/calculate_result', methods=['POST'])
def calculate_result():
    if request.method == "POST":
        input1 = request.form.get('input_number1')
        if input1 is None:
            return render_template()
        input2 = request.form.get('input_number2')
        result = int(input1) * int(input2)
    return render_template('calculator.html', calculated_number=result)


if __name__ == "__main__":
    app.run(debug=True)
