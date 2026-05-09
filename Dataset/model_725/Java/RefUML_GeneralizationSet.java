





import java.util.List;
import java.util.ArrayList;

public class RefUML_GeneralizationSet extends PackageableElement {

    private String isDisjoint;
    private String isCovering;





    private RefUML_Classifier refuml_classifier;




    private RefUML_Classifier refuml_classifier;


    public RefUML_GeneralizationSet(
        String isDisjoint,        String isCovering    ) {
        super(
        );
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
    }


    public String getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(String isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public String getIscovering() {
        return isCovering;
    }

    public void setIscovering(String isCovering) {
        this.isCovering = isCovering;
    }

    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }
    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }

}