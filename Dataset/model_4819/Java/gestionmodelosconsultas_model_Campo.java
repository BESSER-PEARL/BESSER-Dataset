





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_model_Campo  {

    private String criterio;
    private String nombreCampo;
    private boolean seleccion;



    public gestionmodelosconsultas_model_Campo(
        String criterio,        String nombreCampo,        boolean seleccion    ) {
        this.criterio = criterio;
        this.nombreCampo = nombreCampo;
        this.seleccion = seleccion;
    }


    public String getCriterio() {
        return criterio;
    }

    public void setCriterio(String criterio) {
        this.criterio = criterio;
    }
    public String getNombrecampo() {
        return nombreCampo;
    }

    public void setNombrecampo(String nombreCampo) {
        this.nombreCampo = nombreCampo;
    }
    public boolean getSeleccion() {
        return seleccion;
    }

    public void setSeleccion(boolean seleccion) {
        this.seleccion = seleccion;
    }


}