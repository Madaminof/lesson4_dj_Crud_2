from django.shortcuts import render,redirect
from .models import Category,Phones
from .forms import ProductForm
# Create your views here.


def get_info(request):
    categories=Category.objects.all()

    context={'categories':categories}
    return render(request,'index.html',context=context)


def get_Phones(request,pk):
    phone=Phones.objects.filter(category=pk)

    context={'phone':phone}
    return render(request,'phones.html',context=context)



def detail(request,pk):
    product=Phones.objects.get(pk=pk)
    context={'product':product}
    return render(request,'details.html',context=context)





def add_Phones(request):
    form=ProductForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Phones:get_info')
    
    context={
        'form':form
    }
    return render(request,'create.html',context=context)



def update_Phones(request, pk):
    data = Phones.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('Phones:get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)


from django.shortcuts import get_object_or_404

def delete_product(request, pk):
    product = get_object_or_404(Phones, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('Phones:get_info')
    
    return render(request, 'delete.html', {'product': product})





   

   
