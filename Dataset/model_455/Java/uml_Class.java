





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends BehavioredClassifier, EncapsulatedClassifier {

    private String isActive;





    private uml_Operation uml_operation;




    private uml_Property uml_property;




    private List<uml_Classifier> uml_classifiers;




    private List<uml_Class> uml_classs;




    private List<uml_Operation> uml_operations;


    public uml_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml_classifiers = new ArrayList<>();
        this.uml_classs = new ArrayList<>();
        this.uml_operations = new ArrayList<>();
    }

    public uml_Class(
        String isActive        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_Class> uml_classs,        ArrayList<uml_Operation> uml_operations    ) {
        this.isActive = isActive;
        this.uml_classifiers = uml_classifiers;
        this.uml_classs = uml_classs;
        this.uml_operations = uml_operations;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }
    public uml_Property getUml_property() {
        return uml_property;
    }

    public void setUml_property(uml_Property uml_property) {
        this.uml_property = uml_property;
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public List<uml_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }
    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }

}