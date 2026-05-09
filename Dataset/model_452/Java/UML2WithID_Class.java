





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Class extends EncapsulatedClassifier, BehavioredClassifier {

    private boolean isActive;





    private List<UML2WithID_Extension> uml2withid_extensions;




    private UML2WithID_Operation uml2withid_operation;




    private UML2WithID_Extension uml2withid_extension;




    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private List<UML2WithID_Operation> uml2withid_operations;




    private List<UML2WithID_Class> uml2withid_classs;




    private UML2WithID_Property uml2withid_property;


    public UML2WithID_Class(
        boolean isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml2withid_extensions = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
        this.uml2withid_operations = new ArrayList<>();
        this.uml2withid_classs = new ArrayList<>();
    }

    public UML2WithID_Class(
        boolean isActive        ArrayList<UML2WithID_Extension> uml2withid_extensions,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers,        ArrayList<UML2WithID_Operation> uml2withid_operations,        ArrayList<UML2WithID_Class> uml2withid_classs    ) {
        this.isActive = isActive;
        this.uml2withid_extensions = uml2withid_extensions;
        this.uml2withid_classifiers = uml2withid_classifiers;
        this.uml2withid_operations = uml2withid_operations;
        this.uml2withid_classs = uml2withid_classs;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public List<UML2WithID_Extension> getUml2withid_extensions() {
        return uml2withid_extensions;
    }

    public void addUml2withid_extension(Uml2withid_extension uml2withid_extension) {
        this.uml2withid_extensions.add(uml2withid_extension);
    }
    public UML2WithID_Operation getUml2withid_operation() {
        return uml2withid_operation;
    }

    public void setUml2withid_operation(UML2WithID_Operation uml2withid_operation) {
        this.uml2withid_operation = uml2withid_operation;
    }
    public UML2WithID_Extension getUml2withid_extension() {
        return uml2withid_extension;
    }

    public void setUml2withid_extension(UML2WithID_Extension uml2withid_extension) {
        this.uml2withid_extension = uml2withid_extension;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public List<UML2WithID_Class> getUml2withid_classs() {
        return uml2withid_classs;
    }

    public void addUml2withid_class(Uml2withid_class uml2withid_class) {
        this.uml2withid_classs.add(uml2withid_class);
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }

}