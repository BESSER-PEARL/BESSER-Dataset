





import java.util.List;
import java.util.ArrayList;

public class uml2CD_GeneralizationSet  {

    private boolean isDisjoint;
    private boolean isCovering;





    private uml2CD_Classifier uml2cd_classifier;




    private uml2CD_Generalization uml2cd_generalization;




    private uml2CD_Classifier uml2cd_classifier;




    private List<uml2CD_Generalization> uml2cd_generalizations;


    public uml2CD_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering    ) {
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
        this.uml2cd_generalizations = new ArrayList<>();
    }

    public uml2CD_GeneralizationSet(
        boolean isDisjoint,        boolean isCovering        ArrayList<uml2CD_Generalization> uml2cd_generalizations    ) {
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
        this.uml2cd_generalizations = uml2cd_generalizations;
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

    public uml2CD_Classifier getUml2cd_classifier() {
        return uml2cd_classifier;
    }

    public void setUml2cd_classifier(uml2CD_Classifier uml2cd_classifier) {
        this.uml2cd_classifier = uml2cd_classifier;
    }
    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }
    public uml2CD_Classifier getUml2cd_classifier() {
        return uml2cd_classifier;
    }

    public void setUml2cd_classifier(uml2CD_Classifier uml2cd_classifier) {
        this.uml2cd_classifier = uml2cd_classifier;
    }
    public List<uml2CD_Generalization> getUml2cd_generalizations() {
        return uml2cd_generalizations;
    }

    public void addUml2cd_generalization(Uml2cd_generalization uml2cd_generalization) {
        this.uml2cd_generalizations.add(uml2cd_generalization);
    }

}