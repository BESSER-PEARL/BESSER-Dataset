





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_GeneralizationSet extends PackageableElement {

    private boolean isCovering;
    private boolean isDisjoint;





    private UML2WithID_Generalization uml2withid_generalization;




    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_Classifier uml2withid_classifier;




    private List<UML2WithID_Generalization> uml2withid_generalizations;


    public UML2WithID_GeneralizationSet(
        boolean isCovering,        boolean isDisjoint    ) {
        super(
        );
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml2withid_generalizations = new ArrayList<>();
    }

    public UML2WithID_GeneralizationSet(
        boolean isCovering,        boolean isDisjoint        ArrayList<UML2WithID_Generalization> uml2withid_generalizations    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml2withid_generalizations = uml2withid_generalizations;
    }

    public boolean getIscovering() {
        return isCovering;
    }

    public void setIscovering(boolean isCovering) {
        this.isCovering = isCovering;
    }
    public boolean getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(boolean isDisjoint) {
        this.isDisjoint = isDisjoint;
    }

    public UML2WithID_Generalization getUml2withid_generalization() {
        return uml2withid_generalization;
    }

    public void setUml2withid_generalization(UML2WithID_Generalization uml2withid_generalization) {
        this.uml2withid_generalization = uml2withid_generalization;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public List<UML2WithID_Generalization> getUml2withid_generalizations() {
        return uml2withid_generalizations;
    }

    public void addUml2withid_generalization(Uml2withid_generalization uml2withid_generalization) {
        this.uml2withid_generalizations.add(uml2withid_generalization);
    }

}