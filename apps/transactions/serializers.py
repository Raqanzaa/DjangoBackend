# serializers.py

from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'color', 'icon', 'parent']


class TransactionSerializer(serializers.ModelSerializer):
    # This field is now ONLY for handling the input ID when creating/updating.
    # We will control the output (the nested object) in the to_representation method below.
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False # Based on your model (blank=True, null=True)
    )

    class Meta:
        model = Transaction
        fields = [
            'id', 'type', 'amount', 'description',
            'date', 'category', # This name is used for both input and output
            'created_at', 'updated_at'
        ]

    def __init__(self, *args, **kwargs):
        """
        Override to filter the category queryset based on the request user for security.
        """
        super().__init__(*args, **kwargs)
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            user = request.user
            self.fields['category'].queryset = Category.objects.filter(user=user)
    
    def to_representation(self, instance):
        """
        Override to control what the API outputs.
        This method converts the Category ID into a full nested object for GET requests.
        """
        # Get the default serialized data (which would have category as an ID)
        representation = super().to_representation(instance)
        
        # Get the Category object related to the transaction instance
        category_obj = instance.category
        
        # If a category exists, serialize it using CategorySerializer
        if category_obj:
            # The 'context' is passed to handle nested serializers correctly
            representation['category'] = CategorySerializer(category_obj, context=self.context).data
        
        return representation