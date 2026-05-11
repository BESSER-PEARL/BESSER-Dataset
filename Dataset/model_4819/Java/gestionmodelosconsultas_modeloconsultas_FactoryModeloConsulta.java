





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta  {






    private List<ModeloConsulta> modeloconsultas;


    public gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta(
    ) {
        this.modeloconsultas = new ArrayList<>();
    }

    public gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta(
        ArrayList<ModeloConsulta> modeloconsultas    ) {
        this.modeloconsultas = modeloconsultas;
    }


    public List<ModeloConsulta> getModeloconsultas() {
        return modeloconsultas;
    }

    public void addModeloconsulta(Modeloconsulta modeloconsulta) {
        this.modeloconsultas.add(modeloconsulta);
    }

}