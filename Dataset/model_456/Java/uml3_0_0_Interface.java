





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Interface extends Classifier {






    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private List<uml3_0_0_Operation> uml3_0_0_operations;




    private uml3_0_0_Operation uml3_0_0_operation;




    private uml3_0_0_Interface uml3_0_0_interface;


    public uml3_0_0_Interface(
    ) {
        super(
        );
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_operations = new ArrayList<>();
    }

    public uml3_0_0_Interface(
        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_Operation> uml3_0_0_operations    ) {
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_operations = uml3_0_0_operations;
    }


    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public List<uml3_0_0_Operation> getUml3_0_0_operations() {
        return uml3_0_0_operations;
    }

    public void addUml3_0_0_operation(Uml3_0_0_operation uml3_0_0_operation) {
        this.uml3_0_0_operations.add(uml3_0_0_operation);
    }
    public uml3_0_0_Operation getUml3_0_0_operation() {
        return uml3_0_0_operation;
    }

    public void setUml3_0_0_operation(uml3_0_0_Operation uml3_0_0_operation) {
        this.uml3_0_0_operation = uml3_0_0_operation;
    }
    public uml3_0_0_Interface getUml3_0_0_interface() {
        return uml3_0_0_interface;
    }

    public void setUml3_0_0_interface(uml3_0_0_Interface uml3_0_0_interface) {
        this.uml3_0_0_interface = uml3_0_0_interface;
    }

}