





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Generalization extends DirectedRelationship {

    private String isSubstitutable;





    private RefOntoUML_Classifier refontouml_classifier;




    private RefOntoUML_GeneralizationSet refontouml_generalizationset;




    private RefOntoUML_Classifier refontouml_classifier;




    private List<RefOntoUML_GeneralizationSet> refontouml_generalizationsets;




    private RefOntoUML_Classifier refontouml_classifier;


    public RefOntoUML_Generalization(
        String isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
        this.refontouml_generalizationsets = new ArrayList<>();
    }

    public RefOntoUML_Generalization(
        String isSubstitutable        ArrayList<RefOntoUML_GeneralizationSet> refontouml_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.refontouml_generalizationsets = refontouml_generalizationsets;
    }

    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }
    public RefOntoUML_GeneralizationSet getRefontouml_generalizationset() {
        return refontouml_generalizationset;
    }

    public void setRefontouml_generalizationset(RefOntoUML_GeneralizationSet refontouml_generalizationset) {
        this.refontouml_generalizationset = refontouml_generalizationset;
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }
    public List<RefOntoUML_GeneralizationSet> getRefontouml_generalizationsets() {
        return refontouml_generalizationsets;
    }

    public void addRefontouml_generalizationset(Refontouml_generalizationset refontouml_generalizationset) {
        this.refontouml_generalizationsets.add(refontouml_generalizationset);
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }

}