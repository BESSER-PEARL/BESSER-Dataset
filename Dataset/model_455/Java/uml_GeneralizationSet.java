





import java.util.List;
import java.util.ArrayList;

public class uml_GeneralizationSet extends PackageableElement {

    private String isCovering;
    private String isDisjoint;





    private uml_Classifier uml_classifier;




    private List<uml_Generalization> uml_generalizations;




    private uml_Classifier uml_classifier;




    private uml_Generalization uml_generalization;


    public uml_GeneralizationSet(
        String isCovering,        String isDisjoint    ) {
        super(
        );
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml_generalizations = new ArrayList<>();
    }

    public uml_GeneralizationSet(
        String isCovering,        String isDisjoint        ArrayList<uml_Generalization> uml_generalizations    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml_generalizations = uml_generalizations;
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

    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_Generalization> getUml_generalizations() {
        return uml_generalizations;
    }

    public void addUml_generalization(Uml_generalization uml_generalization) {
        this.uml_generalizations.add(uml_generalization);
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public uml_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(uml_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }

}