





import java.util.List;
import java.util.ArrayList;

public class RefUML_GeneralizationSet extends PackageableElement {

    private String isCovering;
    private String isDisjoint;





    private RefUML_Classifier refuml_classifier;




    private RefUML_Classifier refuml_classifier;


    public RefUML_GeneralizationSet(
        String isCovering,        String isDisjoint    ) {
        super(
        );
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
    }


    public String getIscovering() {
        return isCovering;
    }

    public void setIscovering(String isCovering) {
        this.isCovering = isCovering;
    }
    public String getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(String isDisjoint) {
        this.isDisjoint = isDisjoint;
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