





import java.util.List;
import java.util.ArrayList;

public class UML_14_Class extends NamedElement {

    private String isActive;





    private List<UML_14_Method> uml_14_methods;




    private UML_14_Package uml_14_package;




    private UML_14_AssociationEnd uml_14_associationend;


    public UML_14_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml_14_methods = new ArrayList<>();
    }

    public UML_14_Class(
        String isActive        ArrayList<UML_14_Method> uml_14_methods    ) {
        this.isActive = isActive;
        this.uml_14_methods = uml_14_methods;
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
    public UML_14_Package getUml_14_package() {
        return uml_14_package;
    }

    public void setUml_14_package(UML_14_Package uml_14_package) {
        this.uml_14_package = uml_14_package;
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }

}