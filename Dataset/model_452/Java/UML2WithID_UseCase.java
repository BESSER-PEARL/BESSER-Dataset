





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_UseCase extends BehavioredClassifier {






    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_ExtensionPoint uml2withid_extensionpoint;




    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private List<UML2WithID_ExtensionPoint> uml2withid_extensionpoints;




    private UML2WithID_Classifier uml2withid_classifier;


    public UML2WithID_UseCase(
    ) {
        super(
        );
        this.uml2withid_classifiers = new ArrayList<>();
        this.uml2withid_extensionpoints = new ArrayList<>();
    }

    public UML2WithID_UseCase(
        ArrayList<UML2WithID_Classifier> uml2withid_classifiers,        ArrayList<UML2WithID_ExtensionPoint> uml2withid_extensionpoints    ) {
        this.uml2withid_classifiers = uml2withid_classifiers;
        this.uml2withid_extensionpoints = uml2withid_extensionpoints;
    }


    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_ExtensionPoint getUml2withid_extensionpoint() {
        return uml2withid_extensionpoint;
    }

    public void setUml2withid_extensionpoint(UML2WithID_ExtensionPoint uml2withid_extensionpoint) {
        this.uml2withid_extensionpoint = uml2withid_extensionpoint;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public List<UML2WithID_ExtensionPoint> getUml2withid_extensionpoints() {
        return uml2withid_extensionpoints;
    }

    public void addUml2withid_extensionpoint(Uml2withid_extensionpoint uml2withid_extensionpoint) {
        this.uml2withid_extensionpoints.add(uml2withid_extensionpoint);
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }

}