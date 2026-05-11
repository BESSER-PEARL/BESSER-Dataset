





import java.util.List;
import java.util.ArrayList;

public class umlClass_Class extends Classifier {

    private String isActive;





    private umlClass_Operation umlclass_operation;




    private List<umlClass_Classifier> umlclass_classifiers;




    private List<umlClass_Property> umlclass_propertys;




    private umlClass_Association umlclass_association;




    private umlClass_Generalization umlclass_generalization;




    private umlClass_Class umlclass_class;




    private umlClass_Association umlclass_association;




    private List<umlClass_Operation> umlclass_operations;




    private umlClass_Property umlclass_property;




    private umlClass_Generalization umlclass_generalization;


    public umlClass_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.umlclass_classifiers = new ArrayList<>();
        this.umlclass_propertys = new ArrayList<>();
        this.umlclass_operations = new ArrayList<>();
    }

    public umlClass_Class(
        String isActive        ArrayList<umlClass_Classifier> umlclass_classifiers,        ArrayList<umlClass_Property> umlclass_propertys,        ArrayList<umlClass_Operation> umlclass_operations    ) {
        this.isActive = isActive;
        this.umlclass_classifiers = umlclass_classifiers;
        this.umlclass_propertys = umlclass_propertys;
        this.umlclass_operations = umlclass_operations;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public umlClass_Operation getUmlclass_operation() {
        return umlclass_operation;
    }

    public void setUmlclass_operation(umlClass_Operation umlclass_operation) {
        this.umlclass_operation = umlclass_operation;
    }
    public List<umlClass_Classifier> getUmlclass_classifiers() {
        return umlclass_classifiers;
    }

    public void addUmlclass_classifier(Umlclass_classifier umlclass_classifier) {
        this.umlclass_classifiers.add(umlclass_classifier);
    }
    public List<umlClass_Property> getUmlclass_propertys() {
        return umlclass_propertys;
    }

    public void addUmlclass_property(Umlclass_property umlclass_property) {
        this.umlclass_propertys.add(umlclass_property);
    }
    public umlClass_Association getUmlclass_association() {
        return umlclass_association;
    }

    public void setUmlclass_association(umlClass_Association umlclass_association) {
        this.umlclass_association = umlclass_association;
    }
    public umlClass_Generalization getUmlclass_generalization() {
        return umlclass_generalization;
    }

    public void setUmlclass_generalization(umlClass_Generalization umlclass_generalization) {
        this.umlclass_generalization = umlclass_generalization;
    }
    public umlClass_Class getUmlclass_class() {
        return umlclass_class;
    }

    public void setUmlclass_class(umlClass_Class umlclass_class) {
        this.umlclass_class = umlclass_class;
    }
    public umlClass_Association getUmlclass_association() {
        return umlclass_association;
    }

    public void setUmlclass_association(umlClass_Association umlclass_association) {
        this.umlclass_association = umlclass_association;
    }
    public List<umlClass_Operation> getUmlclass_operations() {
        return umlclass_operations;
    }

    public void addUmlclass_operation(Umlclass_operation umlclass_operation) {
        this.umlclass_operations.add(umlclass_operation);
    }
    public umlClass_Property getUmlclass_property() {
        return umlclass_property;
    }

    public void setUmlclass_property(umlClass_Property umlclass_property) {
        this.umlclass_property = umlclass_property;
    }
    public umlClass_Generalization getUmlclass_generalization() {
        return umlclass_generalization;
    }

    public void setUmlclass_generalization(umlClass_Generalization umlclass_generalization) {
        this.umlclass_generalization = umlclass_generalization;
    }

}