from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return render(request, 'calculator/index.html', {'result': None})

@csrf_exempt
def calculate(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Division by zero error'
            else:
                result = 'Invalid operation'
        except ValueError:
            result = 'Invalid input'
        
    # ส่งค่าผลลัพธ์กลับในรูปแบบ JSON
    return JsonResponse({'result': result})