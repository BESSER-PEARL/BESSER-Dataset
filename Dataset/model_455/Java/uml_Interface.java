





import java.util.List;
import java.util.ArrayList;

public class uml_Interface extends Classifier {






    private uml_Operation uml_operation;




    private uml_Interface uml_interface;




    private List<uml_Operation> uml_operations;




    private List<uml_Classifier> uml_classifiers;


    public uml_Interface(
    ) {
        super(
        );
        this.uml_operations = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_Interface(
        ArrayList<uml_Operation> uml_operations,        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.uml_operations = uml_operations;
        this.uml_classifiers = uml_classifiers;
    }


    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }
    public uml_Interface getUml_interface() {
        return uml_interface;
    }

    public void setUml_interface(uml_Interface uml_interface) {
        this.uml_interface = uml_interface;
    }
    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}