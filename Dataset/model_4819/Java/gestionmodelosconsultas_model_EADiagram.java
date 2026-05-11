





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_model_EADiagram  {

    private String nombre;





    private ModeloConsulta modeloconsulta;


    public gestionmodelosconsultas_model_EADiagram(
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