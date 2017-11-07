from rest_framework import generics

from ..models import Snippet
from ..serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # super쓰면 안됨 => 원래있던 로직 실행하면 안됨 (user가 없는 상태에서 save하는 거이므로)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
