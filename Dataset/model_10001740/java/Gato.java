





import java.util.List;
import java.util.ArrayList;

public class Gato  {

    private String ultimaDesparasitacion;
    private String MESES_ENTRE_DESPARASITACIONES;



    public Gato(
        String ultimaDesparasitacion,        String MESES_ENTRE_DESPARASITACIONES    ) {
        this.ultimaDesparasitacion = ultimaDesparasitacion;
        this.MESES_ENTRE_DESPARASITACIONES = MESES_ENTRE_DESPARASITACIONES;
    }


    public String getUltimadesparasitacion() {
        return ultimaDesparasitacion;
    }

    public void setUltimadesparasitacion(String ultimaDesparasitacion) {
        this.ultimaDesparasitacion = ultimaDesparasitacion;
    }
    public String getMeses_entre_desparasitaciones() {
        return MESES_ENTRE_DESPARASITACIONES;
    }

    public void setMeses_entre_desparasitaciones(String MESES_ENTRE_DESPARASITACIONES) {
        this.MESES_ENTRE_DESPARASITACIONES = MESES_ENTRE_DESPARASITACIONES;
    }


}