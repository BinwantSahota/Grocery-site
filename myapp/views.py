from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Type, Item, labmember
from django.shortcuts import get_object_or_404
import calendar
from .forms import OrderItemForm, InterestForm

# Create your views here.
def index(request):
    type_list = Type.objects.all().order_by('id')[:10]
    return render(request,'myapp/index.html',{'type_list':type_list})



# Create your views here.

def about(request, year=None, month=None):
    if year is not None and month is not None:

        month_name = calendar.month_name[int(month)]

        welcome_message = '<p>' + f"This is an Online Grocery Store. You visited in {month_name} {year}." + '</p>'
    else:
        # If year and month are not provided, display a general welcome message
        welcome_message = "This is an Online Grocery Store."

    return render(request, 'myapp/about.html', {'welcome_message': welcome_message})


def detail(request, type_no):
    # Retrieve the type object or raise a 404 error if not found
    type_obj = get_object_or_404(Type, pk=type_no)

    # Retrieve the items associated with the selected type
    items = Item.objects.filter(type=type_obj)

    # Pass necessary variables to the template
    context = {
        'type_obj': type_obj,
        'items': items,
    }

    # Render the detail.html template with the provided context
    return render(request, 'myapp/detail.html', context)


class Detail(View):     #CBV for Part 3

    def get(self, request, type_no):
        response = HttpResponse()
        try:
            selected_type = Type.objects.get(pk=type_no)
            items = Item.objects.filter(type=selected_type)
            for i in items:
                para = '<p>' + str(i) + '</p>'
                response.write(para)
            return response
        except:
            return HttpResponse(status=404)


class labmemberdetails(View):
    def get(self,request):
        details = labmember.objects.all().order_by('-first_name')
        return render(request, 'myapp/labmember.html', {'details': details})


# class dummy(View):
#     def get(self,request):
#         dummy1 = 'dummy1'
#         dummy2 = 'dummy2'
#         context ={'dummy1':'dummy1','dummy2':'dummy2'}
#         return render(request, 'myapp/about.html',context)




def formTest(request):
    if request.method == 'POST':
        order_item_form = OrderItemForm(request.POST)
        interest_form = InterestForm(request.POST)
        if order_item_form.is_valid() and interest_form.is_valid():
            order_item_form.save()

    else:
        order_item_form = OrderItemForm()
        interest_form = InterestForm()
    return render(request, 'myapp/test1.html', {'order_item_form': order_item_form, 'interest_form': interest_form})



def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp/items.html', {'itemlist': itemlist})

def placeorder(request):
    message ='You can place your order here.'
    return render(request, 'myapp/placeorder.html',{'message': message})











# Difference between FBV and CBV explained:

# 1. Function-Based View (FBV) is a simple function that takes a request and returns a response.
# 2. Class-Based View (CBV) is a class that inherits from Django's View class and has methods (like get) for different HTTP methods.
# 3. In FBV, the logic is directly in the function.
# 4. In CBV, the logic is encapsulated in methods (e.g., get method for handling HTTP GET requests).
# 5. CBV allows for more organized code with different methods for different HTTP methods.
# 6. CBV can be extended more easily, for example, by adding additional methods for different actions.
# 7. CBV is often more reusable as the behavior is encapsulated within the class.




# a. Client.objects.filter(last_name='Mir')
# b. Client.objects.filter(shipping_address__contains = '45')
# c. Client.objects.filter(city = 'WD').filter(shipping_address__contains = 'street')
# d. Client.objects.filter(city= 'CH'); Client.objects.filter(city= 'TO')
# e. Client.objects.exclude(city= 'WD')
# f. type = Type.objects.get(name='Bakery')
# Client.objects.filter(interested_in = type)
# g. Item.objects.filter(price__lt = 5.0)
# h. Item.objects.filter(available = False)
# i. Client.objects.get(username = 'saja').interested_in.all()
# j. Item.objects.filter(price__gt = '12').filter(stock__lt = '130')
# k. OrderItem.objects.get(pk = 2).client.first_name
# l. alltype = Type.objects.all()
# alltype.__len__()
# alltype[2]
# m. for i in Type.objects.all():
#     print(i)
# n.coffee_item = Item.objects.get(name = 'Coffee')
# OrderItem.objects.filter(item = coffee_item, status = 1)
# o. OrderItem.objects.get(status = 1).client
# p. Item.objects.filter(price__gt = 5.00).filter(price__lt = 15.00)
# q. Client.objects.filter(orderitem__isnull=False).filter(city__in=['WD','CH'])
# r. from django.db.models import Avg
# type_instance = Type.objects.get(name='Bakery')
# Item.objects.filter(type=type_instance).aggregate(average_price=Avg('price'))['average_price']
# s. from django.db.models import Sum
# type_instance = Type.objects.get(name='Bakery')
# Item.objects.filter(type=type_instance).aggregate(total_items=Sum('stock'))[    'total_items']
