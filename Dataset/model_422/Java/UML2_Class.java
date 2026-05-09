





import java.util.List;
import java.util.ArrayList;

public class UML2_Class extends BehavioredClassifier, EncapsulatedClassifier {

    private boolean isActive;





    private List<UML2_Classifier> uml2_classifiers;




    private List<UML2_Reception> uml2_receptions;


    public UML2_Class(
        boolean isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_receptions = new ArrayList<>();
    }

    public UML2_Class(
        boolean isActive        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_Reception> uml2_receptions    ) {
        this.isActive = isActive;
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_receptions = uml2_receptions;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public List<UML2_Reception> getUml2_receptions() {
        return uml2_receptions;
    }

    public void addUml2_reception(Uml2_reception uml2_reception) {
        this.uml2_receptions.add(uml2_reception);
    }

}