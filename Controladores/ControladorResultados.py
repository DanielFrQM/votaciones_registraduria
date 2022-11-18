from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Modelos.Resultados import Resultados

class ControladorResultados():


    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        print("Creando Controlado de Resultados")


    def create(self, infoResultados, id_candidato, id_mesa):
        print("crear Resultado")
        crearResultados = Resultados(infoResultados)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        crearResultados.candidato = candidato
        crearResultados.mesa = mesa
        return self.repositorioResultados.save(crearResultados)
    #
    def mostrarResultado(self, id):
        print("Mostrando el Resultados con ID:"+str(id))
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def mostrarResultados(self):
        print("Listar todos los Resultados")
        return self.repositorioResultados.findAll()

    def delete(self, id):
        print("Se elimino el Resultados con el id: "+str(id))
        return self.repositorioResultados.delete(id)

    def update(self,id,ResultadosDatos,id_candidato,id_mesa):
        print("Se Actualizo el Resultados con id: "+str(id))
        resultado = Resultados(self.repositorioResultados.findById(id))
        resultado.numeromesa= ResultadosDatos["numeromesa"]
        resultado.partido = ResultadosDatos["partido"]
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultado.candidato = candidato
        resultado.materia = mesa
        return self.repositorioResultados.save(resultado)

    def listarResultados(self):
        return self.repositorioResultados.getListadoResultadocandidato()

    def listarResultadoMesa(self,id_mesa):
        return self.repositorioResultados.getListadoResultadoporMesa(id_mesa)

    def numerototalpormesa(self):
        return self.repositorioResultados.getSumademesas()

    def resultadopartido(self):
        return self.repositorioResultados.getListadoResultadopartidopolitico()

    def resultadopartidopormesa(self,id_mesa):
        return self.repositorioResultados.getListadoPartidoporMesa(id_mesa)

    def resultadoporcentajepartido(self):
        return self.repositorioResultados.getListadoporcentajepartidopolitico()

