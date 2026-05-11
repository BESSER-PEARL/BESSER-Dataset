





import java.util.List;
import java.util.ArrayList;

public class UML_14_MultiplicityRange  {

    private String lower;
    private String upper;





    private UML_14_Attribute uml_14_attribute;




    private UML_14_AssociationEnd uml_14_associationend;


    public UML_14_MultiplicityRange(
        String lower,        String upper    ) {
        this.lower = lower;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public UML_14_Attribute getUml_14_attribute() {
        return uml_14_attribute;
    }

    public void setUml_14_attribute(UML_14_Attribute uml_14_attribute) {
        this.uml_14_attribute = uml_14_attribute;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }

}