from django import forms
from .models import *


class product_form(forms.ModelForm):
    class Meta:
        model = products
        # fields="__all__"
        exclude=['vendor']
        labels={
            'product_name' : "Product_Name",
            'product_price' : "Product_Price",
            'product_image' : "Product_Image",
            "product_category" : "Product_Category",
            "MFG_Date" : "MFG_Date",
            "stock" : "Stock",
            "piece" : "Piece",
            "product_old_price" : "Old_Price",
            "vendor":"Vendor",
        }
        widgets={
            "vendor": forms.Select(attrs={"required":"False"}),
            "product_name" : forms.TextInput(attrs={"placeholder": "Enter Product Name"}),
            "product_price" : forms.NumberInput(attrs={"placeholder": "Enter Product Price"}),
            "product_image" : forms.ClearableFileInput(attrs={"placeholder": "Enter Product Image"}),
            "product_category" : forms.Select(),
            "MFG_Date" : forms.DateTimeInput(),
            "stock" : forms.NumberInput(attrs={"placeholder" : "Enter Product's Stock"}),
            "piece" : forms.NumberInput(attrs={"placeholder" : "Enter Number of Piece"}),
            "product_old_price" : forms.NumberInput(attrs={"placeholder" : "Enter Product's Old Price"})
        }
