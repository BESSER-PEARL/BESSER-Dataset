





import java.util.List;
import java.util.ArrayList;

public class UML_14_Attribute extends NamedElement {

    private String visibility;
    private String initialValue;





    private UML_14_Enumeration uml_14_enumeration;




    private UML_14_Class uml_14_class;




    private UML_14_Primitive uml_14_primitive;




    private UML_14_AssociationEnd uml_14_associationend;


    public UML_14_Attribute(
        String visibility,        String initialValue    ) {
        super(
        );
        this.visibility = visibility;
        this.initialValue = initialValue;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }

    public UML_14_Enumeration getUml_14_enumeration() {
        return uml_14_enumeration;
    }

    public void setUml_14_enumeration(UML_14_Enumeration uml_14_enumeration) {
        this.uml_14_enumeration = uml_14_enumeration;
    }
    public UML_14_Class getUml_14_class() {
        return uml_14_class;
    }

    public void setUml_14_class(UML_14_Class uml_14_class) {
        this.uml_14_class = uml_14_class;
    }
    public UML_14_Primitive getUml_14_primitive() {
        return uml_14_primitive;
    }

    public void setUml_14_primitive(UML_14_Primitive uml_14_primitive) {
        this.uml_14_primitive = uml_14_primitive;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }

}