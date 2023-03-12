from django.shortcuts import render,redirect
from .forms import *
from django.conf import settings
from django.contrib import messages
from Vendor.models import *
from .models import *


# Create your views here.


#Product Profile Function
def product_profile(request):
        if request.session.get('admin') == None:
            return redirect("Vendor:v-login")
        usr=User.objects.get(username=request.session.get("admin_uname"))
        company=usr.vendor_name.vendor_profile_model.company_name
        if request.method == "POST":
            pif=product_form(request.POST,request.FILES)
            if pif.is_valid():
                temp=pif.save(commit=False)
                user = User.objects.get(username = request.session.get('admin_uname'))
                temp.vendor=user
                # temp.company_name=user.vendor_name.vendor_profile_model.company_name
                temp.save()
                messages.success(request,"Product Details Saved Successfully!")
                return redirect("products:p-dashboard")
            else:
                messages.error(request,"Invalid Input!")
        else:
            pif=product_form()
        product_form()
        user = User.objects.get(username = request.session.get('admin_uname'))
        # c_name=Vendor_profile_model.objects.get()
        data=products.objects.all()
        template="products/profile.html"
        return render(request,template,{"form": pif,"data": data,"company":company})



#Product update
def update_data(request,id):
    uid=products.objects.get(pk=id)
    if request.method == "POST":
        uf=product_form(request.POST,request.FILES,instance=uid)
        if uf.is_valid():
            uf.save()
            messages.success(request,"Data Has Been Updated Successfully!")
            # return redirect("products:p-profile")
            uf=product_form()
            return redirect("products:p-dashboard")
        else:
            messages.error(request,"Invalid Input!")
    else:
        uf=product_form(instance=uid)
    # data=products.objects.all()
    template="Vendor/update-data.html"
    return render(request,template,{"form" : uf })


#Delete Product

def remove_data(request,id):
    id=products.objects.get(pk=id)
    id.delete()
    return redirect('products:p-dashboard')

#Vendor Product Page
def dashboard(request):
    if request.session.get("admin_uname") == None:
        return redirect("Vendor:v-login")
    user=User.objects.get(username=request.session.get('admin_uname'))
    data=products.objects.all().filter(vendor=user)
    c_data=Vendor_profile_model.objects.get(vendor=user.vendor_name.vendor_profile_model.vendor)
    print(c_data)
    print(data)
    template='Vendor/dashboard.html'
    return render(request,template,{"data": data,"c_data":c_data})


#Single Product
def product_details(request,id):
    usr=User.objects.get(username=request.session.get("admin_uname"))
    company=usr.vendor_name.vendor_profile_model.company_name
    print(company)
    v_data=usr.vendor_name.vendor_profile_model.contact_no
    print(v_data)
    prod=products.objects.get(pk=id)
    template="Vendor/product-details.html"
    return render(request,template,{"products":prod,"company":company,"v_data":v_data})

# def index(request):
#     p_data=products.objects.all()
#     user=User.objects.get(username=request.session.get('admin_uname'))
#     c_data=Vendor_profile_model.objects.get(vendor=user.vendor_name.vendor_profile_model.vendor)
#     template="index.html"
#     return render(request,template,{"p_data":p_data,"c_data":c_data})