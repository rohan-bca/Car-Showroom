from django.shortcuts import render, redirect, get_object_or_404
from .models import CarModel, CarRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



@login_required(login_url='login')
def car_list(request):
    cars = CarModel.objects.all()
    return render(request, 'website/cars.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        CarModel.objects.create(
            name=request.POST.get("name"),
            brand=request.POST.get("brand"),
            price=request.POST.get("price"),
            model_year=request.POST.get("model_year"),
            fuel_type=request.POST.get("fuel_type"),
            color=request.POST.get("color"),
            description=request.POST.get("description"),
        )
        return redirect('car_list')

    return render(request, 'website/add_car.html')


def edit_car(request, id):
    car = get_object_or_404(CarModel, id=id)

    if request.method == 'POST':
        car.name = request.POST.get("name")
        car.brand = request.POST.get("brand")
        car.price = request.POST.get("price")
        car.model_year = request.POST.get("model_year")
        car.fuel_type = request.POST.get("fuel_type")
        car.color = request.POST.get("color")
        car.description = request.POST.get("description")
        car.save()

        return redirect('car_list')

    return render(request, 'website/edit_car.html', {'car': car})


def delete_car(request, id):
    car = get_object_or_404(CarModel, id=id)
    car.delete()
    return redirect('car_list')




def register_car(request):
    if request.method == "POST":

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        car_name = request.POST.get('car_name')
        car_model = request.POST.get('car_model')
        fuel_type = request.POST.get('fuel_type')
        color = request.POST.get('color')
        nearest_showroom = request.POST.get('nearest_showroom')

        # Save data
        CarRegistration.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            car_name=car_name,
            car_model=car_model,
            fuel_type=fuel_type,
            color=color,
            nearest_showroom=nearest_showroom
        )

        # Send email to user
        send_mail(
            subject="Car Booking Confirmation - CarWale",
            message=(
                f"Hello {full_name},\n\n"
                "Your car booking has been successfully registered.\n\n"
                f"Car Name: {car_name}\n"
                f"Car Model: {car_model}\n"
                f"Fuel Type: {fuel_type}\n"
                f"Color: {color}\n"
                f"Showroom: {nearest_showroom}\n\n"
                "Our team will contact you shortly.\n\n"
                "Thank you for choosing CarWale!"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Car booked successfully! Confirmation email sent.")
        # return redirect('registrations_list')

    return render(request, 'website/register.html')





def registrations_list(request):
    registrations = CarRegistration.objects.all()
    return render(request, 'website/registrations.html', {
        'registrations': registrations
    })

from django.shortcuts import render

def register(request):
    return render(request, 'website/register.html')


def home(request):
    cars = [
        {'id': 1, 'name': 'Mahindra XEV 9S', 'price':'Rs. 19.95 - 29.45 Lakh', 'showroom': 'Showroom : PUNE',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/212003/xev9s-exterior-right-front-three-quarter-11.png?isig=0&q=80'},

        {'id': 2, 'name': 'Hyundai Venue', 'price':'Rs. 7.0 - 15 Lakh', 'showroom': 'Showroom: MUMBAI',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/197163/venue-exterior-right-front-three-quarter-38.png?isig=0&q=80'},

        {'id': 3, 'name': 'Mahindra XUV 3XO','price':'Rs. 7.28 - 14.40 Lakh', 'showroom': 'Showroom: NASHIK',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/156405/xuv-3xo-exterior-right-front-three-quarter-33.png?isig=0&q=80'},

        {'id': 4, 'name': 'Maruti Fronx','price':'Rs. 6.85 - 11.98 Lakh', 'showroom': 'Showroom: PUNE',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/130591/fronx-exterior-right-front-three-quarter-109.png?isig=0&q=80'},

        {'id': 5, 'name': 'Volkswagen Taigun','price':'Rs. 11.42 - 19.19 Lakh', 'showroom': 'Showroom: SATARA',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/144689/taigun-exterior-right-front-three-quarter-8.png?isig=0&q=80'},
        
        {'id': 6, 'name': 'Jeep Compass','price':'Rs. 17.73 - 30.58 Lakh', 'showroom': 'Showroom: NASHIK',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/45278/xuv400-exterior-right-front-three-quarter-8.png?isig=0&q=80'},

        {'id': 7, 'name': 'Tesla Model Y','price':'Rs. 59.89 - 67.89 Lakh', 'showroom': 'Showroom: PUNE',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/186465/ev6-exterior-right-front-three-quarter-3.png?isig=0&q=80',
        },        
        {'id': 8, 'name': 'Kia EV9','price':'Rs. 1.30 - 1.50 Crore', 'showroom': 'Showroom: MUMBAI',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/144485/ev9-exterior-right-front-three-quarter-6.png?isig=0&q=80',
        },
    ]

    return render(request, 'website/index.html', {'cars': cars})


def car_detail(request, car_id):
    cars = [
        {'id': 1, 'name': 'Mahindra XEV 9S', 'price':'Rs. 19.95 - 29.45 Lakh', 'showroom': 'PUNE',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/212003/xev9s-exterior-right-front-three-quarter-11.png?isig=0&q=80',
         'description': "Mahindra XEV 9S is an electric SUV with premium features."},

        {'id': 2, 'name': 'Hyundai Venue', 'price':'Rs. 7.0 - 15 Lakh', 'showroom': 'MUMBAI',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/197163/venue-exterior-right-front-three-quarter-38.png?isig=0&q=80',
         'description': "The Hyundai Venue is a compact SUV with modern tech."},

        {'id': 3, 'name': 'Mahindra XUV 3XO','price':'Rs. 7.28 - 14.40 Lakh', 'showroom': 'NASHIK',
         'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/156405/xuv-3xo-exterior-right-front-three-quarter-33.png?isig=0&q=80',
         'description': "The new XUV 3XO offers strong performance and features."},

        {'id': 4, 'name': 'Maruti Fronx','price':'Rs. 6.85 - 11.98 Lakh', 'showroom': 'PUNE',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/130591/fronx-exterior-right-front-three-quarter-109.png?isig=0&q=80',
        'description': "Maruti Fronx is a stylish crossover with good mileage."},
        {'id': 5, 'name': 'Volkswagen Taigun','price':'Rs. 11.42 - 19.19 Lakh', 'showroom': 'SATARA',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/144689/taigun-exterior-right-front-three-quarter-8.png?isig=0&q=80',
        'description': "The Volkswagen Taigun has an excellent ride quality, especially on the highways."},
        
        {'id': 6, 'name': 'Jeep Compass','price':'Rs. 17.73 - 30.58 Lakh', 'showroom': 'Showroom: NASHIK',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/45278/xuv400-exterior-right-front-three-quarter-8.png?isig=0&q=80',
        'description': "The Jeep Compass gets the iconic seven-slat grille, 18-inch alloys, and angular wheel arches to command a bold road presence."
        },
        {'id': 7, 'name': 'Tesla Model Y','price':'Rs. 59.89 - 67.89 Lakh', 'showroom': 'Showroom: PUNE',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/186465/ev6-exterior-right-front-three-quarter-3.png?isig=0&q=80',
        'description': "The Jeep Compass gets the iconic seven-slat grille, 18-inch alloys, and angular wheel arches to command a bold road presence."
        },
        {'id': 8, 'name': 'Kia EV9','price':'Rs. 1.30 - 1.50 Crore', 'showroom': 'Showroom: MUMBAI',
        'image':'https://imgd.aeplcdn.com/664x374/n/cw/ec/144485/ev9-exterior-right-front-three-quarter-6.png?isig=0&q=80',
        'description': "It gets features such as a trinity display setup, large sunroof, lavish massage seats with boss function, and independent climate zones."
        },

    ]

    car = next((c for c in cars if c['id'] == car_id), None)

    return render(request, 'website/car_detail.html', {'car': car})



def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmed_password = request.POST.get("confirmed_password")

        # Password match check
        if password != confirmed_password:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("signup")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Optional email
        send_mail(
            subject="Registration Successful",
            message=f"Hello {username}, your account has been created successfully.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "website/signup.html")




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("car_list")  # change if needed
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "website/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')



