from .models import Shipping,Shipping_Cargo,Cargo, User
from rest_framework import serializers
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['pk','title' , 'price_per_ton', 'short_description' , 'description', 'is_active', 'logo_file_path']
        read_only_fields = ['pk']
    
class getCargoSerializer(serializers.Serializer):
     cargo = CargoSerializer(many=True)
     shipping_id = serializers.IntegerField(required=False,allow_null=True)
     items_in_cart = serializers.IntegerField()

# class Client_Serialzier(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ["id", "username"]

class ShippingSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()

    class Meta:
        model = Shipping
        fields = ['pk',"creation_datetime", 'status', "completion_datetime" , 'formation_datetime' ,  'client', 'manager' , 'organization' ,'total_price']
        # read_only_fields = ['status']
    def get_client(self, obj):
        return obj.client.username

class Shipping_CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Cargo
        fields = ['shipping', 'cargo', 'amount']

class ResolveShipping(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ['status']


class Adding_to_shippingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Shipping
            fields = ['pk',"creation_datetime",  "completion_datetime" , 'client', 'manager' , 'organization' ,'total_price' ,'status']
            read_only_fields = ['pk',"creation_datetime",  "completion_datetime" , 'client', 'manager'  ,'total_price', 'status']
            extra_kwargs = {
            'organization': {'read_only': False}
        }



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username',   'password']
        read_only_fields = ['id']


class UpdateUserSerializer(serializers.ModelSerializer):
     username = serializers.CharField(required=False, allow_blank=True)
     email = serializers.EmailField(required=False, allow_blank=True)
     password = serializers.CharField(write_only=True, required=False, allow_blank=True)

     class Meta : 
          model = User
          fields = ['username', 'email', 'password']
          extra_kwargs = {
            'password': {'write_only': True}
        }


# class Cargo_for_shippingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cargo
#         fields = ["pk", "title",  "short_description", "logo_file_path"]


class connection_Serializer(serializers.ModelSerializer):
      cargo = serializers.SerializerMethodField()
      def get_cargo(self, obj):
           return {
            'pk' : obj.id,
            "title": obj.cargo.title,
            "short_description": obj.cargo.short_description,
            "description" : obj.cargo.description,
            "price_per_ton" : obj.cargo.price_per_ton,
            "logo_file_path": obj.cargo.logo_file_path,
        }
      class Meta:
            model = Shipping_Cargo
            fields = ["cargo", 'amount']  


class CargosForRequestedSerializer(serializers.ModelSerializer):
     class Meta:
          model = Cargo
          fields = ['pk', 'title', 'price_per_ton', 'logo_file_path']
          
class RelatedSerializer(serializers.ModelSerializer):
     cargo = CargosForRequestedSerializer()
     class Meta:
          model = Shipping_Cargo
          fields = ['cargo', 'amount']

class Shipping_with_info_Serializer(serializers.ModelSerializer):
        cargo_list = RelatedSerializer(source='shipping_cargo_set', many=True)

        # def get_cargo_list(self, obj):
        #     cargo_list = connection_Serializer(obj.shipping_cargo_set, many=True).data
        #     amount_list = [cargo['amount'] for cargo in cargo_list]

        #     cargo_list = [cargo['cargo'] for cargo in cargo_list]
        #     for i,cargo in enumerate(cargo_list):
        #          cargo['amount'] = amount_list[i]
            
        #     print(type(cargo_list))
        #     return cargo_list
        class Meta:
            model = Shipping
            fields = ['pk', "creation_datetime",  "completion_datetime" , 'client', 'manager' , 'organization', 'cargo_list', 'status', "formation_datetime"]