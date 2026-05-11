





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_modeloconsultas_ModeloConsulta  {

    private String nombre;





    private FactoryModeloConsulta factorymodeloconsulta;




    private RealizacionDiagramEntity realizaciondiagramentity;


    public gestionmodelosconsultas_modeloconsultas_ModeloConsulta(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public FactoryModeloConsulta getFactorymodeloconsulta() {
        return factorymodeloconsulta;
    }

    public void setFactorymodeloconsulta(FactoryModeloConsulta factorymodeloconsulta) {
        this.factorymodeloconsulta = factorymodeloconsulta;
    }
    public RealizacionDiagramEntity getRealizaciondiagramentity() {
        return realizaciondiagramentity;
    }

    public void setRealizaciondiagramentity(RealizacionDiagramEntity realizaciondiagramentity) {
        this.realizaciondiagramentity = realizaciondiagramentity;
    }

}