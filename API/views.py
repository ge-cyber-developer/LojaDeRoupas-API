from rest_framework.views import APIView
from rest_framework.response import Response
from . import models


class PecaView(APIView):
    def get(self, request,id= None):
        if id:
            peca = models.Peca.objects.get(id=id)
            peca = {
                "id" : peca.id,
                "nome" : peca.nome,
                "tamanho" : peca.tamanho
            }
        else:
            peca = models.Peca.objects.all().values("id", "nome","tamanho")
        
        return Response(peca)


    def post(self, request):
        nome = request.data["nome"]
        tamanho = request.data["tamanho"]
        peca = models.Peca(nome = nome, tamanho = tamanho)
        peca.save()
        return Response("Salvamos uma peça")


    def delete(self, request, id):
        peca = models.Peca.objects.get(id = id)
        peca.delete()
        return Response("Deletamos uma peca")
        



