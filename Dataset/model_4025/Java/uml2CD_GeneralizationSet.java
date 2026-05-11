





import java.util.List;
import java.util.ArrayList;

public class uml2CD_GeneralizationSet  {

    private String isCovering;
    private String isDisjoint;





    private List<uml2CD_Generalization> uml2cd_generalizations;




    private uml2CD_Generalization uml2cd_generalization;


    public uml2CD_GeneralizationSet(
        String isCovering,        String isDisjoint    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml2cd_generalizations = new ArrayList<>();
    }

    public uml2CD_GeneralizationSet(
        String isCovering,        String isDisjoint        ArrayList<uml2CD_Generalization> uml2cd_generalizations    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
        this.uml2cd_generalizations = uml2cd_generalizations;
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

    public List<uml2CD_Generalization> getUml2cd_generalizations() {
        return uml2cd_generalizations;
    }

    public void addUml2cd_generalization(Uml2cd_generalization uml2cd_generalization) {
        this.uml2cd_generalizations.add(uml2cd_generalization);
    }
    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }

}