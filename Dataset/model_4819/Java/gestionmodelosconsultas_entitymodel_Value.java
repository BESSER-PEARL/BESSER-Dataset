





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_Value  {

    private String value;





    private RealizacionDiagramEntity realizaciondiagramentity;




    private List<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes;


    public gestionmodelosconsultas_entitymodel_Value(
        String value    ) {
        this.value = value;
        this.elementorealizacionvalueattributes = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_Value(
        String value        ArrayList<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes    ) {
        this.value = value;
        this.elementorealizacionvalueattributes = elementorealizacionvalueattributes;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public RealizacionDiagramEntity getRealizaciondiagramentity() {
        return realizaciondiagramentity;
    }

    public void setRealizaciondiagramentity(RealizacionDiagramEntity realizaciondiagramentity) {
        this.realizaciondiagramentity = realizaciondiagramentity;
    }
    public List<ElementoRealizacionValueAttribute> getElementorealizacionvalueattributes() {
        return elementorealizacionvalueattributes;
    }

    public void addElementorealizacionvalueattribute(Elementorealizacionvalueattribute elementorealizacionvalueattribute) {
        this.elementorealizacionvalueattributes.add(elementorealizacionvalueattribute);
    }

}