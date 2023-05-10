from django import forms

class AddItemForm(forms.Form):
    name = forms.CharField(max_length=200, label='Tên hàng')
    description = forms.CharField(widget=forms.Textarea, label='Mô tả')
    thumbnail = forms.ImageField(label='Hình ảnh bìa')
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'accept': 'image/*'}), label='Hình ảnh')
    price = forms.IntegerField(label='Giá')

    def clean(self):
        super(AddItemForm, self).clean()

        price = self.cleaned_data['price']

        if float(price) < 0:
            self._errors['price'] = self.error_class(['Giá không thể nhỏ hơn 0'])
        return self.cleaned_data