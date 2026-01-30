from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        values = request.form.getlist("numbers")
        numbers = [float(v) for v in values if v != ""]

        operation = request.form["operation"]

        if operation == "add":
            result = sum(numbers)

        elif operation == "mul":
            result = 1
            for n in numbers:
                result *= n

        elif operation == "sub":
            result = numbers[0]
            for n in numbers[1:]:
                result -= n

        elif operation == "div":
            result = numbers[0]
            for n in numbers[1:]:
                if n == 0:
                    result = "Error: Division by zero"
                    break
                result /= n

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()