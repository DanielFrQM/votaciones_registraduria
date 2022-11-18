from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):

    def getListResultadosCandidato(self, id_candidato):
        query = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(query)

    def getListadoResultadoporMesa(self,id_mesa):
        query1 = {
            "$match": {
                "mesa.$id": ObjectId(id_mesa)
            }
        }
        query2 = {
            "$sort": {
                "numero_mesa": -1
            }
        }

        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    def getListadoResultadocandidato(self):
        query2 = {
            "$sort":{
                "numero_mesa":-1
            }
        }

        pipeline = [query2]
        return self.queryAggregation(pipeline)

    def getSumademesas(self):
        query1 = {
            "$group": {
                "_id": "$mesa","suma": {
                    "$sum": "$numero_mesa"
                }
            }
        }
        query2 = {
            "$sort": {
                "numero_mesa": 1
                      }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    def getListadoResultadopartidopolitico(self):
        query1 = {
            "$group": {
                "_id": "$id_partido","suma": {
                    "$sum": "$numero_mesa"
                }
            }
        }
        query2 = {
            "$sort": {
                "suma": -1
            }
        }

        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    def getListadoPartidoporMesa(self,id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$id_partido","suma": {
                    "$sum": "$numero_mesa"
                }
            }
        }

        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    def getListadoporcentajepartidopolitico(self):
        query1 = {
            "$group": {
                "_id": "$id_partido", "media": {
                    "$sum": "$numero_mesa"
                }
            }
        }
        query2 = {
            "$project": {
                "multiplicar": {
                    "$multiply": ["$media", 100]
                }
            }
        }
        query3 = {
            "$project": {
                "porcentaje": {
                    "$divide": ["$multiplicar", 3600]
                }
            }
        }

        pipeline = [query1,query2,query3]
        return self.queryAggregation(pipeline)