





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Interface extends Classifier {






    private List<UML2WithID_Property> uml2withid_propertys;




    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private List<UML2WithID_Operation> uml2withid_operations;




    private List<UML2WithID_Reception> uml2withid_receptions;




    private UML2WithID_Implementation uml2withid_implementation;




    private List<UML2WithID_Interface> uml2withid_interfaces;


    public UML2WithID_Interface(
    ) {
        super(
        );
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
        this.uml2withid_operations = new ArrayList<>();
        this.uml2withid_receptions = new ArrayList<>();
        this.uml2withid_interfaces = new ArrayList<>();
    }

    public UML2WithID_Interface(
        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers,        ArrayList<UML2WithID_Operation> uml2withid_operations,        ArrayList<UML2WithID_Reception> uml2withid_receptions,        ArrayList<UML2WithID_Interface> uml2withid_interfaces    ) {
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_classifiers = uml2withid_classifiers;
        this.uml2withid_operations = uml2withid_operations;
        this.uml2withid_receptions = uml2withid_receptions;
        this.uml2withid_interfaces = uml2withid_interfaces;
    }


    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public List<UML2WithID_Reception> getUml2withid_receptions() {
        return uml2withid_receptions;
    }

    public void addUml2withid_reception(Uml2withid_reception uml2withid_reception) {
        this.uml2withid_receptions.add(uml2withid_reception);
    }
    public UML2WithID_Implementation getUml2withid_implementation() {
        return uml2withid_implementation;
    }

    public void setUml2withid_implementation(UML2WithID_Implementation uml2withid_implementation) {
        this.uml2withid_implementation = uml2withid_implementation;
    }
    public List<UML2WithID_Interface> getUml2withid_interfaces() {
        return uml2withid_interfaces;
    }

    public void addUml2withid_interface(Uml2withid_interface uml2withid_interface) {
        this.uml2withid_interfaces.add(uml2withid_interface);
    }

}