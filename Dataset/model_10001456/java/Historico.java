





import java.util.List;
import java.util.ArrayList;

public class Historico  {

    private int numeroPartidosGanados;
    private String porcentajeApuestasEnFavor;
    private int numeroPartidosPerdidos;
    private int numeroPartidosJugados;





    private List<Partido> partidos;




    private Equipo equipo;


    public Historico(
        int numeroPartidosGanados,        String porcentajeApuestasEnFavor,        int numeroPartidosPerdidos,        int numeroPartidosJugados    ) {
        this.numeroPartidosGanados = numeroPartidosGanados;
        this.porcentajeApuestasEnFavor = porcentajeApuestasEnFavor;
        this.numeroPartidosPerdidos = numeroPartidosPerdidos;
        this.numeroPartidosJugados = numeroPartidosJugados;
        this.partidos = new ArrayList<>();
    }

    public Historico(
        int numeroPartidosGanados,        String porcentajeApuestasEnFavor,        int numeroPartidosPerdidos,        int numeroPartidosJugados        ArrayList<Partido> partidos    ) {
        this.numeroPartidosGanados = numeroPartidosGanados;
        this.porcentajeApuestasEnFavor = porcentajeApuestasEnFavor;
        this.numeroPartidosPerdidos = numeroPartidosPerdidos;
        this.numeroPartidosJugados = numeroPartidosJugados;
        this.partidos = partidos;
    }

    public int getNumeropartidosganados() {
        return numeroPartidosGanados;
    }

    public void setNumeropartidosganados(int numeroPartidosGanados) {
        this.numeroPartidosGanados = numeroPartidosGanados;
    }
    public String getPorcentajeapuestasenfavor() {
        return porcentajeApuestasEnFavor;
    }

    public void setPorcentajeapuestasenfavor(String porcentajeApuestasEnFavor) {
        this.porcentajeApuestasEnFavor = porcentajeApuestasEnFavor;
    }
    public int getNumeropartidosperdidos() {
        return numeroPartidosPerdidos;
    }

    public void setNumeropartidosperdidos(int numeroPartidosPerdidos) {
        this.numeroPartidosPerdidos = numeroPartidosPerdidos;
    }
    public int getNumeropartidosjugados() {
        return numeroPartidosJugados;
    }

    public void setNumeropartidosjugados(int numeroPartidosJugados) {
        this.numeroPartidosJugados = numeroPartidosJugados;
    }

    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }
    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}