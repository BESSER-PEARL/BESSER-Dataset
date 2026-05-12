





import java.util.List;
import java.util.ArrayList;

public class ApuestaMarcadorEspecifico  {

    private int numeroGolesEquipo2;
    private String porcentajeAciertoMarcador;
    private int numeroGolesEquipo1;
    private String nombreEquipoGanador;



    public ApuestaMarcadorEspecifico(
        int numeroGolesEquipo2,        String porcentajeAciertoMarcador,        int numeroGolesEquipo1,        String nombreEquipoGanador    ) {
        this.numeroGolesEquipo2 = numeroGolesEquipo2;
        this.porcentajeAciertoMarcador = porcentajeAciertoMarcador;
        this.numeroGolesEquipo1 = numeroGolesEquipo1;
        this.nombreEquipoGanador = nombreEquipoGanador;
    }


    public int getNumerogolesequipo2() {
        return numeroGolesEquipo2;
    }

    public void setNumerogolesequipo2(int numeroGolesEquipo2) {
        this.numeroGolesEquipo2 = numeroGolesEquipo2;
    }
    public String getPorcentajeaciertomarcador() {
        return porcentajeAciertoMarcador;
    }

    public void setPorcentajeaciertomarcador(String porcentajeAciertoMarcador) {
        this.porcentajeAciertoMarcador = porcentajeAciertoMarcador;
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


}