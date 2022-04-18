from rest_framework import viewsets, mixins


class CreateRetrieveViewset(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    pass
