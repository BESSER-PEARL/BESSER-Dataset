





import java.util.List;
import java.util.ArrayList;

public class UML_14_StructuralFeature extends Feature {

    private String ordering;
    private String targetScope;
    private String changeability;





    private UML_14_Classifier uml_14_classifier;




    private UML_14_Classifier uml_14_classifier;


    public UML_14_StructuralFeature(
        String ordering,        String targetScope,        String changeability    ) {
        super(
        );
        this.ordering = ordering;
        this.targetScope = targetScope;
        this.changeability = changeability;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public String getTargetscope() {
        return targetScope;
    }

    public void setTargetscope(String targetScope) {
        this.targetScope = targetScope;
    }
    public String getChangeability() {
        return changeability;
    }

    public void setChangeability(String changeability) {
        this.changeability = changeability;
    }

    public UML_14_Classifier getUml_14_classifier() {
        return uml_14_classifier;
    }

    public void setUml_14_classifier(UML_14_Classifier uml_14_classifier) {
        this.uml_14_classifier = uml_14_classifier;
    }
    public UML_14_Classifier getUml_14_classifier() {
        return uml_14_classifier;
    }

    public void setUml_14_classifier(UML_14_Classifier uml_14_classifier) {
        this.uml_14_classifier = uml_14_classifier;
    }

}