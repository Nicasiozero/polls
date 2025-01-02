from django.shortcuts import render

def index(request):
    return render(request, 'calculator/index.html', {'result': None})

# def calculate(request):
#     result = None
#     if request.method == "POST":
#         try:
#             num1 = float(request.POST.get('num1', 0))
#             num2 = float(request.POST.get('num2', 0))
#             operation = request.POST.get('operation')
            
#             if operation == 'add':
#                 result = num1 + num2
#             elif operation == 'subtract':
#                 result = num1 - num2
#             elif operation == 'multiply':
#                 result = num1 * num2
#             elif operation == 'divide':
#                 result = num1 / num2 if num2 != 0 else 'Division by zero error'
#             else:
#                 result = 'Invalid operation'
#         except ValueError:
#             result = 'Invalid input'
            
#     return render(request, 'calculator/index.html', {'result': result})
