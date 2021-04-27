from rest_framework.serializers import IntegerField,CharField,Serializer,ModelSerializer,\
    ImageField, HyperlinkedIdentityField,SlugRelatedField

from blog.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ThinPostSerializer(ModelSerializer):   #for shorter view
    url = HyperlinkedIdentityField(view_name="posts-detail", lookup_field="slug")     #for urls in api view page
    class Meta:
        model = Post
        fields = ("id", "title", "url")






# class PostSerializer(Serializer):
#     id = IntegerField(read_only=True)
#     title = CharField(max_length=255,)
#     # slug = SlugField(max_length=255, unique=True)
#     author = CharField(max_length=100,)
#     content = CharField(required=False, allow_blank=True)
#     photo = ImageField()
#
#     def create(self, validated_data):
#        return Post.objects.create(**validated_data)              #inpacked data
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.author = validated_data.get("author",instance.author )
#         instance.content = validated_data.get("content",instance.content)
#         instance.photo = validated_data.get("photo", instance.photo)
#         instance.save()
#         return instance

