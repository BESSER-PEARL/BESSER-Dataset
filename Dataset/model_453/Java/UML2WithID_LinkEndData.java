





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_LinkEndData extends Element {






    private List<UML2WithID_QualifierValue> uml2withid_qualifiervalues;


    public UML2WithID_LinkEndData(
    ) {
        super(
        );
        this.uml2withid_qualifiervalues = new ArrayList<>();
    }

    public UML2WithID_LinkEndData(
        ArrayList<UML2WithID_QualifierValue> uml2withid_qualifiervalues    ) {
        this.uml2withid_qualifiervalues = uml2withid_qualifiervalues;
    }


    public List<UML2WithID_QualifierValue> getUml2withid_qualifiervalues() {
        return uml2withid_qualifiervalues;
    }

    public void addUml2withid_qualifiervalue(Uml2withid_qualifiervalue uml2withid_qualifiervalue) {
        this.uml2withid_qualifiervalues.add(uml2withid_qualifiervalue);
    }

}