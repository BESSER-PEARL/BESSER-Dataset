





import java.util.List;
import java.util.ArrayList;

public class UML2_UseCase extends BehavioredClassifier {






    private UML2_Classifier uml2_classifier;




    private List<UML2_ExtensionPoint> uml2_extensionpoints;




    private UML2_ExtensionPoint uml2_extensionpoint;




    private List<UML2_Classifier> uml2_classifiers;




    private UML2_Classifier uml2_classifier;


    public UML2_UseCase(
    ) {
        super(
        );
        this.uml2_extensionpoints = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_UseCase(
        ArrayList<UML2_ExtensionPoint> uml2_extensionpoints,        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.uml2_extensionpoints = uml2_extensionpoints;
        this.uml2_classifiers = uml2_classifiers;
    }


    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public List<UML2_ExtensionPoint> getUml2_extensionpoints() {
        return uml2_extensionpoints;
    }

    public void addUml2_extensionpoint(Uml2_extensionpoint uml2_extensionpoint) {
        this.uml2_extensionpoints.add(uml2_extensionpoint);
    }
    public UML2_ExtensionPoint getUml2_extensionpoint() {
        return uml2_extensionpoint;
    }

    public void setUml2_extensionpoint(UML2_ExtensionPoint uml2_extensionpoint) {
        this.uml2_extensionpoint = uml2_extensionpoint;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}