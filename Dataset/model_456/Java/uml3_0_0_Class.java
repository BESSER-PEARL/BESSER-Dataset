





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Class extends EncapsulatedClassifier, BehavioredClassifier {

    private String isActive;





    private List<uml3_0_0_Operation> uml3_0_0_operations;




    private uml3_0_0_Operation uml3_0_0_operation;




    private uml3_0_0_Property uml3_0_0_property;




    private uml3_0_0_Class uml3_0_0_class;




    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;


    public uml3_0_0_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml3_0_0_operations = new ArrayList<>();
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_Class(
        String isActive        ArrayList<uml3_0_0_Operation> uml3_0_0_operations,        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.isActive = isActive;
        this.uml3_0_0_operations = uml3_0_0_operations;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
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
    public uml3_0_0_Property getUml3_0_0_property() {
        return uml3_0_0_property;
    }

    public void setUml3_0_0_property(uml3_0_0_Property uml3_0_0_property) {
        this.uml3_0_0_property = uml3_0_0_property;
    }
    public uml3_0_0_Class getUml3_0_0_class() {
        return uml3_0_0_class;
    }

    public void setUml3_0_0_class(uml3_0_0_Class uml3_0_0_class) {
        this.uml3_0_0_class = uml3_0_0_class;
    }
    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }

}