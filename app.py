from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2

        except Exception as e:
            result = "Error: " + str(e)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()