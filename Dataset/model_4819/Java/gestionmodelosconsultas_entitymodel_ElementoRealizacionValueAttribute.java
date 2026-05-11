





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute  {

    private String nombre;





    private ElementoRealizacionDiagramEntity elementorealizaciondiagramentity;




    private List<Attribute> attributes;


    public gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute(
        String nombre    ) {
        this.nombre = nombre;
        this.attributes = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute(
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

    public ElementoRealizacionDiagramEntity getElementorealizaciondiagramentity() {
        return elementorealizaciondiagramentity;
    }

    public void setElementorealizaciondiagramentity(ElementoRealizacionDiagramEntity elementorealizaciondiagramentity) {
        this.elementorealizaciondiagramentity = elementorealizaciondiagramentity;
    }
    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}