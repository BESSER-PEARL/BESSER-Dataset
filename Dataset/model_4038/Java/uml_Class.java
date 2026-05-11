





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends Classifier {

    private String isAbstract;





    private List<uml_Property> uml_propertys;




    private List<uml_Operation> uml_operations;




    private List<uml_Classifier> uml_classifiers;




    private List<uml_Classifier> uml_classifiers;


    public uml_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml_propertys = new ArrayList<>();
        this.uml_operations = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_Class(
        String isAbstract        ArrayList<uml_Property> uml_propertys,        ArrayList<uml_Operation> uml_operations,        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.isAbstract = isAbstract;
        this.uml_propertys = uml_propertys;
        this.uml_operations = uml_operations;
        this.uml_classifiers = uml_classifiers;
        this.uml_classifiers = uml_classifiers;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<uml_Property> getUml_propertys() {
        return uml_propertys;
    }

    public void addUml_property(Uml_property uml_property) {
        this.uml_propertys.add(uml_property);
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
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}