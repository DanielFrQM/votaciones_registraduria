from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    pass
    # def getListResultadosCandidato(self, id_candidato):
    #     query = {"Candidato.$id": ObjectId(id_candidato)}
    #     return self.query(query)
    # def getListadoInscritosEnMateria(self, id_materia):
    #     theQuery = {"materia.$id": ObjectId(id_materia)}
    #     return self.query(theQuery)
    #
    # def getMayorNotaporCurso(self):
    #     query = {
    #         "$group": {
    #             "_id": "$materia",
    #             "max": {
    #                 "$max": "$nota_final"
    #             },
    #             "doc": {
    #                 "$first": "$$ROOT"
    #             }
    #         }
    #     }
    #     pipeline = [query]
    #     return self.queryAggregation(pipeline)
    #
    # def promedioNotasEnMateria(self, id_materia):
    #     query1 = {
    #         "$match": {"materia.$id": ObjectId(id_materia)}
    #     }
    #     query2 = {
    #         "$group": {
    #             "_id": "$materia",
    #             "promedio": {
    #                 "$avg": "$nota_final"
    #             }
    #         }
    #     }
    #     pipeline = [query1, query2]
    #     return self.queryAggregation(pipeline)