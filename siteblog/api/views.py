import datetime
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
# this ^ to merge all funcs to 1 class
from rest_framework.response import Response
from slugify import slugify

from blog.models import Post
from api.serializers import PostSerializer, ThinPostSerializer, UserSerializer, CitySerializer, OccupationSerializer, \
    VacancySerializer
from jobscrapper.models import City, Occupation, Vacancy
from .permissions import IsAuthorOrReadOnly


# from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
# can use ^ mixins + GenericAPi to get rid of funcs: get,post etc


class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


# class + mixins based further simplification
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthorOrReadOnly,)

    # use this to restrict to only get method(ALLOW: GET in api web page header)
    # http_method_names = ["get"]

    # def list(self, request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     context = {'request': request}
    #     serializer = ThinPostSerializer(posts, many=True, context=context)
    #     return Response(serializer.data)
    def get_serializer_class(self):
        if self.action == "list":
            return ThinPostSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(slug=slugify(self.request.POST["title"]), )


period = datetime.date.today() - datetime.timedelta(1)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OccupationViewSet(ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        city_slug = self.request.query_params.get("city", None)
        occupation_slug = self.request.query_params.get("occupation", None)
        qs = None
        if city_slug and occupation_slug:
            qs = Vacancy.objects.filter(city__slug=city_slug).filter(occupation__slug=occupation_slug,
                                                                     timestamp__gte=period)

        self.queryset = qs
        return self.queryset
