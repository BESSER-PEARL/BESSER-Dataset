





import java.util.List;
import java.util.ArrayList;

public class UML2_LinkEndData extends Element {






    private List<UML2_QualifierValue> uml2_qualifiervalues;




    private UML2_Property uml2_property;


    public UML2_LinkEndData(
    ) {
        super(
        );
        this.uml2_qualifiervalues = new ArrayList<>();
    }

    public UML2_LinkEndData(
        ArrayList<UML2_QualifierValue> uml2_qualifiervalues    ) {
        this.uml2_qualifiervalues = uml2_qualifiervalues;
    }


    public List<UML2_QualifierValue> getUml2_qualifiervalues() {
        return uml2_qualifiervalues;
    }

    public void addUml2_qualifiervalue(Uml2_qualifiervalue uml2_qualifiervalue) {
        this.uml2_qualifiervalues.add(uml2_qualifiervalue);
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }

}