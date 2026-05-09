





import java.util.List;
import java.util.ArrayList;

public class UMLModel_LinkEndData extends Element {

    private String value;
    private String end;





    private List<UMLModel_QualifierValue> umlmodel_qualifiervalues;




    private UMLModel_LinkAction umlmodel_linkaction;


    public UMLModel_LinkEndData(
        String value,        String end    ) {
        super(
        );
        this.value = value;
        this.end = end;
        this.umlmodel_qualifiervalues = new ArrayList<>();
    }

    public UMLModel_LinkEndData(
        String value,        String end        ArrayList<UMLModel_QualifierValue> umlmodel_qualifiervalues    ) {
        this.value = value;
        this.end = end;
        this.umlmodel_qualifiervalues = umlmodel_qualifiervalues;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public List<UMLModel_QualifierValue> getUmlmodel_qualifiervalues() {
        return umlmodel_qualifiervalues;
    }

    public void addUmlmodel_qualifiervalue(Umlmodel_qualifiervalue umlmodel_qualifiervalue) {
        this.umlmodel_qualifiervalues.add(umlmodel_qualifiervalue);
    }
    public UMLModel_LinkAction getUmlmodel_linkaction() {
        return umlmodel_linkaction;
    }

    public void setUmlmodel_linkaction(UMLModel_LinkAction umlmodel_linkaction) {
        this.umlmodel_linkaction = umlmodel_linkaction;
    }

}