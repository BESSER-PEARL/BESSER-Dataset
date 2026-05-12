





import java.util.List;
import java.util.ArrayList;

public class mundo_Neornithe  {

    private String BAJO;
    private String MEDIO;
    private String rangoMetabolico;
    private String densidadOsea;
    private String ALTO;
    private String longitudCola;



    public mundo_Neornithe(
        String BAJO,        String MEDIO,        String rangoMetabolico,        String densidadOsea,        String ALTO,        String longitudCola    ) {
        this.BAJO = BAJO;
        this.MEDIO = MEDIO;
        this.rangoMetabolico = rangoMetabolico;
        this.densidadOsea = densidadOsea;
        this.ALTO = ALTO;
        this.longitudCola = longitudCola;
    }


    public String getBajo() {
        return BAJO;
    }

    public void setBajo(String BAJO) {
        this.BAJO = BAJO;
    }
    public String getMedio() {
        return MEDIO;
    }

    public void setMedio(String MEDIO) {
        this.MEDIO = MEDIO;
    }
    public String getRangometabolico() {
        return rangoMetabolico;
    }

    public void setRangometabolico(String rangoMetabolico) {
        this.rangoMetabolico = rangoMetabolico;
    }
    public String getDensidadosea() {
        return densidadOsea;
    }

    public void setDensidadosea(String densidadOsea) {
        this.densidadOsea = densidadOsea;
    }
    public String getAlto() {
        return ALTO;
    }

    public void setAlto(String ALTO) {
        this.ALTO = ALTO;
    }
    public String getLongitudcola() {
        return longitudCola;
    }

    public void setLongitudcola(String longitudCola) {
        this.longitudCola = longitudCola;
    }


}