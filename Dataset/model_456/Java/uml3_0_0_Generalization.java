





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Generalization extends DirectedRelationship {

    private String isSubstitutable;





    private uml3_0_0_Classifier uml3_0_0_classifier;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private List<uml3_0_0_GeneralizationSet> uml3_0_0_generalizationsets;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private uml3_0_0_GeneralizationSet uml3_0_0_generalizationset;


    public uml3_0_0_Generalization(
        String isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
        this.uml3_0_0_generalizationsets = new ArrayList<>();
    }

    public uml3_0_0_Generalization(
        String isSubstitutable        ArrayList<uml3_0_0_GeneralizationSet> uml3_0_0_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.uml3_0_0_generalizationsets = uml3_0_0_generalizationsets;
    }

    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public List<uml3_0_0_GeneralizationSet> getUml3_0_0_generalizationsets() {
        return uml3_0_0_generalizationsets;
    }

    public void addUml3_0_0_generalizationset(Uml3_0_0_generalizationset uml3_0_0_generalizationset) {
        this.uml3_0_0_generalizationsets.add(uml3_0_0_generalizationset);
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public uml3_0_0_GeneralizationSet getUml3_0_0_generalizationset() {
        return uml3_0_0_generalizationset;
    }

    public void setUml3_0_0_generalizationset(uml3_0_0_GeneralizationSet uml3_0_0_generalizationset) {
        this.uml3_0_0_generalizationset = uml3_0_0_generalizationset;
    }

}