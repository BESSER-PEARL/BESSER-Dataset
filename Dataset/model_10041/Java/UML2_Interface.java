





import java.util.List;
import java.util.ArrayList;

public class UML2_Interface extends Classifier {






    private List<UML2_Classifier> uml2_classifiers;




    private UML2_Interface uml2_interface;




    private List<UML2_Property> uml2_propertys;




    private List<UML2_Reception> uml2_receptions;




    private List<UML2_Operation> uml2_operations;


    public UML2_Interface(
    ) {
        super(
        );
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
        this.uml2_receptions = new ArrayList<>();
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_Interface(
        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Reception> uml2_receptions,        ArrayList<UML2_Operation> uml2_operations    ) {
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_propertys = uml2_propertys;
        this.uml2_receptions = uml2_receptions;
        this.uml2_operations = uml2_operations;
    }


    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_Interface getUml2_interface() {
        return uml2_interface;
    }

    public void setUml2_interface(UML2_Interface uml2_interface) {
        this.uml2_interface = uml2_interface;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public List<UML2_Reception> getUml2_receptions() {
        return uml2_receptions;
    }

    public void addUml2_reception(Uml2_reception uml2_reception) {
        this.uml2_receptions.add(uml2_reception);
    }
    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }

}