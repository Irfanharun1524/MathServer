# Ex.05 Design a Website for Server Side Processing
## Date: 22.05.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

math.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Server</title>
    <style>
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }
        body {
            /* background: linear-gradient(to top, #6e0595, #410ee9); */
            background-color: black;
        }
        .mask {
            width: 700px;
            height: 700px;
            border-radius: 450px;
            left: 0;
            bottom: -2;
            background: linear-gradient(to top, #6e0595, #410ee9);
            clip-path: circle(700px at 50% 50%);
            z-index: 0;
            position: absolute;
        }
        .background{
            font-family: Arial, Helvetica, sans-serif;
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            z-index: 1000;
            position: relative;
        }    
        h1 {
            color: #fff;
            margin-bottom: 30px;
            text-align: center;
            z-index: 1;
        }
    
        .container {
            background-color: rgba(255, 255, 255, 0.518);
            backdrop-filter: blur(15px);
            height: 500px;
            width: 50vw;
            padding: 30px 30px 30px 30px;
            border-radius: 57px;
            background: linear-gradient(#fff2, transparent);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 25px 25px rgba(0, 0, 0, 0.25);
            z-index: 0;
        }
    
        .box {
            color: #fff;
            display: flex;
            height: 40px;
            margin-top: 10px;
            justify-content: space-between;
        }
        .buttons {
            height: 40px;
        }
        .cal {
            height: 30px;
            width: 100px;
            color: #fff;
            border-radius: 15px;
            background-color: rgba(70, 70, 70, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 2% 3% 45% 45%;
            justify-content: space-around;
        }
        .cal:hover {

            box-shadow: 0px 0px 10px rgb(255, 255, 255);
            background: linear-gradient(to right, #6e0595, #410ee9);
            transition: 0.3s;
        }
        .intensity, .resistance, .power {
            background-color: #d5d4d9ab;
            color: #fff;
            height: 30px;
            width: 300px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 2% 3% 45% 45%;
            justify-content: space-around;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="background">
        <div class="mask"></div>
        <div class="container">
            <h1>Power of a lamp filament</h1>
            <form method="post">
                {% csrf_token %}
                <div class="box">
                    Intensity:<input type="text" name="Intensity" value="{{I}}" class="intensity"></input></br>
                </div>
                <div class="box">
                    Resistance:
                    <input type="text" name="Resistance" value="{{R}}" class="resistance">
                    </input></br>
                </div>
                <div>
                    <div class="buttons">
                        <input type="submit" value="Calculate" class="cal">
                        </input>
                        </br>
                    </div>
                </div>
                <div class="box">
                    Power:
                    <input type="text" name="Power" value="{{power}}" class="power">
                    </input></br>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
```

urls.py

```py
from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="calculatepower"),
    path('',views.power,name="calculatepower")
]
```

views.py

```py
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
```

## SERVER SIDE PROCESSING:

![alt text](image-1.png)

## HOMEPAGE:

![alt text](image.png)

## RESULT:
The program for performing server side processing is completed successfully.
