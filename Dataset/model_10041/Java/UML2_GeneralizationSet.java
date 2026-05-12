





import java.util.List;
import java.util.ArrayList;

public class UML2_GeneralizationSet extends PackageableElement {

    private boolean isDisjoint;
    private boolean isCovering;





    private UML2_Classifier uml2_classifier;




    private UML2_Classifier uml2_classifier;


    public UML2_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering    ) {
        super(
        );
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
    }


    public boolean getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(boolean isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public boolean getIscovering() {
        return isCovering;
    }

    public void setIscovering(boolean isCovering) {
        this.isCovering = isCovering;
    }

    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}