from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import AddItemForm

from base.models import Item, Images

# Create your views here.
def User_validator(user):
    if user.is_anonymous or not user.info.admin:
        return False
    return True


class AdminPage(View):
    def get(self, request):
        if not User_validator(self.request.user):
            return redirect('home')
        return render(request, 'adminpanel/admin.html')
    
class PostItem(View):
    def get(self, request):
        if not User_validator(self.request.user):
            return redirect('home')
        form = AddItemForm()
        return render(request, 'adminpanel/additem.html', {
            'form': form,
        })
    
    def post(self, request):
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            field = {}
            images = request.FILES.getlist('images')
            for i in form:
                field[i.name] = form.cleaned_data[i.name]
            create_item = Item(
                title=field['name'], 
                description=field['description'], 
                thumbnail=field['thumbnail'],
                price=field['price'],
            )
            create_item.save()
            
            for image in images:
                post_image = Images(image=image, item=create_item)
                post_image.save()
        
        return render(request, 'adminpanel/additem.html', {
            'form': form
        })