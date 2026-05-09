





import java.util.List;
import java.util.ArrayList;

public class RefUML_Generalization extends DirectedRelationship {

    private String isSubstitutable;





    private RefUML_Classifier refuml_classifier;




    private List<RefUML_GeneralizationSet> refuml_generalizationsets;




    private RefUML_Classifier refuml_classifier;




    private RefUML_GeneralizationSet refuml_generalizationset;




    private RefUML_Classifier refuml_classifier;


    public RefUML_Generalization(
        String isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
        this.refuml_generalizationsets = new ArrayList<>();
    }

    public RefUML_Generalization(
        String isSubstitutable        ArrayList<RefUML_GeneralizationSet> refuml_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.refuml_generalizationsets = refuml_generalizationsets;
    }

    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }
    public List<RefUML_GeneralizationSet> getRefuml_generalizationsets() {
        return refuml_generalizationsets;
    }

    public void addRefuml_generalizationset(Refuml_generalizationset refuml_generalizationset) {
        this.refuml_generalizationsets.add(refuml_generalizationset);
    }
    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }
    public RefUML_GeneralizationSet getRefuml_generalizationset() {
        return refuml_generalizationset;
    }

    public void setRefuml_generalizationset(RefUML_GeneralizationSet refuml_generalizationset) {
        this.refuml_generalizationset = refuml_generalizationset;
    }
    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }

}