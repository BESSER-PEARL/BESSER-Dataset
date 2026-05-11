





import java.util.List;
import java.util.ArrayList;

public class uml2CD_GeneralizationSet  {

    private String isDisjoint;
    private String isCovering;





    private uml2CD_Generalization uml2cd_generalization;


    public uml2CD_GeneralizationSet(
        String isDisjoint,        String isCovering    ) {
        this.isDisjoint = isDisjoint;
        this.isCovering = isCovering;
    }


    public String getIsdisjoint() {
        return isDisjoint;
    }

    public void setIsdisjoint(String isDisjoint) {
        this.isDisjoint = isDisjoint;
    }
    public String getIscovering() {
        return isCovering;
    }

    public void setIscovering(String isCovering) {
        this.isCovering = isCovering;
    }

    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }

}