





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Generalization extends DirectedRelationship {

    private boolean isSubstitutable;





    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_GeneralizationSet uml2withid_generalizationset;




    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_Classifier uml2withid_classifier;




    private List<UML2WithID_GeneralizationSet> uml2withid_generalizationsets;


    public UML2WithID_Generalization(
        boolean isSubstitutable    ) {
        super(
        );
        this.isSubstitutable = isSubstitutable;
        this.uml2withid_generalizationsets = new ArrayList<>();
    }

    public UML2WithID_Generalization(
        boolean isSubstitutable        ArrayList<UML2WithID_GeneralizationSet> uml2withid_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.uml2withid_generalizationsets = uml2withid_generalizationsets;
    }

    public boolean getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(boolean isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_GeneralizationSet getUml2withid_generalizationset() {
        return uml2withid_generalizationset;
    }

    public void setUml2withid_generalizationset(UML2WithID_GeneralizationSet uml2withid_generalizationset) {
        this.uml2withid_generalizationset = uml2withid_generalizationset;
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
    public List<UML2WithID_GeneralizationSet> getUml2withid_generalizationsets() {
        return uml2withid_generalizationsets;
    }

    public void addUml2withid_generalizationset(Uml2withid_generalizationset uml2withid_generalizationset) {
        this.uml2withid_generalizationsets.add(uml2withid_generalizationset);
    }

}