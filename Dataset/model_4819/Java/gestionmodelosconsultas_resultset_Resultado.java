





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultset_Resultado  {

    private String nombre;





    private ModeloConsulta modeloconsulta;


    public gestionmodelosconsultas_resultset_Resultado(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public ModeloConsulta getModeloconsulta() {
        return modeloconsulta;
    }

    public void setModeloconsulta(ModeloConsulta modeloconsulta) {
        this.modeloconsulta = modeloconsulta;
    }

}