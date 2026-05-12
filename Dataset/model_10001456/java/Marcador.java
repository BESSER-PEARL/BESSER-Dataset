





import java.util.List;
import java.util.ArrayList;

public class Marcador  {

    private int numeroGolesEquipo1;
    private String nombreEquipoGanador;
    private int numeroGolesEquipo2;





    private Partido partido;


    public Marcador(
        int numeroGolesEquipo1,        String nombreEquipoGanador,        int numeroGolesEquipo2    ) {
        this.numeroGolesEquipo1 = numeroGolesEquipo1;
        this.nombreEquipoGanador = nombreEquipoGanador;
        this.numeroGolesEquipo2 = numeroGolesEquipo2;
    }


    public int getNumerogolesequipo1() {
        return numeroGolesEquipo1;
    }

    public void setNumerogolesequipo1(int numeroGolesEquipo1) {
        this.numeroGolesEquipo1 = numeroGolesEquipo1;
    }
    public String getNombreequipoganador() {
        return nombreEquipoGanador;
    }

    public void setNombreequipoganador(String nombreEquipoGanador) {
        this.nombreEquipoGanador = nombreEquipoGanador;
    }
    public int getNumerogolesequipo2() {
        return numeroGolesEquipo2;
    }

    public void setNumerogolesequipo2(int numeroGolesEquipo2) {
        this.numeroGolesEquipo2 = numeroGolesEquipo2;
    }

    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }

}