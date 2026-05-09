





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Class extends EncapsulatedClassifier, BehavioredClassifier {

    private String isActive;
    private String extension;
    private String superclass;





    private List<UMLModel_Operation> umlmodel_operations;




    private List<UMLModel_Classifier> umlmodel_classifiers;


    public UMLModel_Class(
        String isActive,        String extension,        String superclass    ) {
        super(
        );
        this.isActive = isActive;
        this.extension = extension;
        this.superclass = superclass;
        this.umlmodel_operations = new ArrayList<>();
        this.umlmodel_classifiers = new ArrayList<>();
    }

    public UMLModel_Class(
        String isActive,        String extension,        String superclass        ArrayList<UMLModel_Operation> umlmodel_operations,        ArrayList<UMLModel_Classifier> umlmodel_classifiers    ) {
        this.isActive = isActive;
        this.extension = extension;
        this.superclass = superclass;
        this.umlmodel_operations = umlmodel_operations;
        this.umlmodel_classifiers = umlmodel_classifiers;
    }

    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getSuperclass() {
        return superclass;
    }

    public void setSuperclass(String superclass) {
        this.superclass = superclass;
    }

    public List<UMLModel_Operation> getUmlmodel_operations() {
        return umlmodel_operations;
    }

    public void addUmlmodel_operation(Umlmodel_operation umlmodel_operation) {
        this.umlmodel_operations.add(umlmodel_operation);
    }
    public List<UMLModel_Classifier> getUmlmodel_classifiers() {
        return umlmodel_classifiers;
    }

    public void addUmlmodel_classifier(Umlmodel_classifier umlmodel_classifier) {
        this.umlmodel_classifiers.add(umlmodel_classifier);
    }

}