from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['R'] = "0" 
    context['I'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        R = request.POST.get('Resistance','0')
        I = request.POST.get('Intensity','0')
        print('request=',request) 
        print('Resistance=',R) 
        print('Intensity=',I) 
        power = int(R) * int(I) * int(I)
        context['power'] = power
        context['R'] = R
        context['I'] = I
        print('Power=',power) 
    return render(request,'myapp/math.html',context)
