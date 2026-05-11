





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends EncapsulatedClassifier, BehavioredClassifier {






    private List<uml_Classifier> uml_classifiers;




    private List<uml_Operation> uml_operations;


    public uml_Class(
    ) {
        super(
        );
        this.uml_classifiers = new ArrayList<>();
        this.uml_operations = new ArrayList<>();
    }

    public uml_Class(
        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_Operation> uml_operations    ) {
        this.uml_classifiers = uml_classifiers;
        this.uml_operations = uml_operations;
    }


    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }

}