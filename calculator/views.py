from django.shortcuts import render


def index(request):
    result = calculate(request)
    return render(request, "index.html", {"result": result})


def calculate(request):
    result = 0
    num1 = float(request.POST.get("num1"))
    num2 = float(request.POST.get("num2"))
    operator = request.POST.get("operator")
    if request.method == "POST":
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                result = "Error: Division by zero"

    return result
