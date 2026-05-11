





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute  {

    private String nombre;





    private RealizacionDiagramEntity realizaciondiagramentity;




    private List<Attribute> attributes;


    public gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute(
        String nombre    ) {
        this.nombre = nombre;
        this.attributes = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute(
        String nombre        ArrayList<Attribute> attributes    ) {
        this.nombre = nombre;
        this.attributes = attributes;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public RealizacionDiagramEntity getRealizaciondiagramentity() {
        return realizaciondiagramentity;
    }

    public void setRealizaciondiagramentity(RealizacionDiagramEntity realizaciondiagramentity) {
        this.realizaciondiagramentity = realizaciondiagramentity;
    }
    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}