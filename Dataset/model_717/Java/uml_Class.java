





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends Classifier {

    private String name;
    private String isActive;





    private List<uml_Classifier> uml_classifiers;




    private List<uml_Generalization> uml_generalizations;




    private uml_Class uml_class;


    public uml_Class(
        String name,        String isActive    ) {
        super(
        );
        this.name = name;
        this.isActive = isActive;
        this.uml_classifiers = new ArrayList<>();
        this.uml_generalizations = new ArrayList<>();
    }

    public uml_Class(
        String name,        String isActive        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_Generalization> uml_generalizations    ) {
        this.name = name;
        this.isActive = isActive;
        this.uml_classifiers = uml_classifiers;
        this.uml_generalizations = uml_generalizations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }

    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public List<uml_Generalization> getUml_generalizations() {
        return uml_generalizations;
    }

    public void addUml_generalization(Uml_generalization uml_generalization) {
        this.uml_generalizations.add(uml_generalization);
    }
    public uml_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(uml_Class uml_class) {
        this.uml_class = uml_class;
    }

}