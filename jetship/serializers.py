from rest_framework import serializers
from .models import Post,Category,Subcategory,Driver,Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['phone_number', 'role', 'name', 'surname', 'village',]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'category', 'category_link']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['subcategory', 'subcategory_link']

class PostSerializer(serializers.ModelSerializer):
    user = GuestSerializer()
    category = CategorySerializer()
    subcategory = SubcategorySerializer()

    class Meta:
        model = Post
        fields = '__all__'
