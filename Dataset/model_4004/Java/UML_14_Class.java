





import java.util.List;
import java.util.ArrayList;

public class UML_14_Class extends NamedElement {

    private String isActive;





    private List<UML_14_Method> uml_14_methods;




    private List<UML_14_Attribute> uml_14_attributes;




    private UML_14_Generalization uml_14_generalization;




    private UML_14_Generalization uml_14_generalization;


    public UML_14_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml_14_methods = new ArrayList<>();
        this.uml_14_attributes = new ArrayList<>();
    }

    public UML_14_Class(
        String isActive        ArrayList<UML_14_Method> uml_14_methods,        ArrayList<UML_14_Attribute> uml_14_attributes    ) {
        this.isActive = isActive;
        this.uml_14_methods = uml_14_methods;
        this.uml_14_attributes = uml_14_attributes;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public List<UML_14_Method> getUml_14_methods() {
        return uml_14_methods;
    }

    public void addUml_14_method(Uml_14_method uml_14_method) {
        this.uml_14_methods.add(uml_14_method);
    }
    public List<UML_14_Attribute> getUml_14_attributes() {
        return uml_14_attributes;
    }

    public void addUml_14_attribute(Uml_14_attribute uml_14_attribute) {
        this.uml_14_attributes.add(uml_14_attribute);
    }
    public UML_14_Generalization getUml_14_generalization() {
        return uml_14_generalization;
    }

    public void setUml_14_generalization(UML_14_Generalization uml_14_generalization) {
        this.uml_14_generalization = uml_14_generalization;
    }
    public UML_14_Generalization getUml_14_generalization() {
        return uml_14_generalization;
    }

    public void setUml_14_generalization(UML_14_Generalization uml_14_generalization) {
        this.uml_14_generalization = uml_14_generalization;
    }

}