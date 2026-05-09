





import java.util.List;
import java.util.ArrayList;

public class UML2_Generalization extends DirectedRelationship {

    private boolean isSubstitutable;





    private UML2_GeneralizationSet uml2_generalizationset;




    private UML2_Classifier uml2_classifier;




    private UML2_Classifier uml2_classifier;




    private List<UML2_GeneralizationSet> uml2_generalizationsets;




    private UML2_Classifier uml2_classifier;


    public UML2_Generalization(
        boolean isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
        this.uml2_generalizationsets = new ArrayList<>();
    }

    public UML2_Generalization(
        boolean isSubstitutable        ArrayList<UML2_GeneralizationSet> uml2_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.uml2_generalizationsets = uml2_generalizationsets;
    }

    public boolean getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(boolean isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public UML2_GeneralizationSet getUml2_generalizationset() {
        return uml2_generalizationset;
    }

    public void setUml2_generalizationset(UML2_GeneralizationSet uml2_generalizationset) {
        this.uml2_generalizationset = uml2_generalizationset;
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
    public List<UML2_GeneralizationSet> getUml2_generalizationsets() {
        return uml2_generalizationsets;
    }

    public void addUml2_generalizationset(Uml2_generalizationset uml2_generalizationset) {
        this.uml2_generalizationsets.add(uml2_generalizationset);
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}