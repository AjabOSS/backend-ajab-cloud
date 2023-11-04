# from importlib.resources import read_binary
# from itertools import product
from rest_framework import serializers
# from  storeapp.models import Cart, Cartitems, Category, Product, Review, ProImage

from content.models import Content
from .models import Branch



class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'branch', 'data']
    
    
class BranchSerializer(serializers.ModelSerializer):
    images = ContentSerializer(many=True, read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(
            max_length = 1000000, 
            allow_empty_file = False,
            use_url = False),
        write_only=True
    )
    
    class Meta:
        model = Branch
        fields = ['id', 'title', 'description', 'author', 'images', 'uploaded_images']
        extra_kwargs = {
            "author":{'read_only':True},
            "title":{'required':True},
        }
    def create(self, validated_data, user):
        uploaded_images = validated_data.pop('uploaded_images')
        # validated_data['']
        # del validated_data['']
        validated_data['author']=user
        branch = Branch.objects.create(**validated_data)
        for image in uploaded_images:
            new_content = Content.objects.create(
                branch=branch,
                data=image,
            )
        return branch