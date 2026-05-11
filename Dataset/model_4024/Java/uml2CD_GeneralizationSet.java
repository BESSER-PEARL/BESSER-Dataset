





import java.util.List;
import java.util.ArrayList;

public class uml2CD_GeneralizationSet  {

    private String isCovering;
    private String isDisjoint;



    public uml2CD_GeneralizationSet(
        String isCovering,        String isDisjoint    ) {
        this.isCovering = isCovering;
        this.isDisjoint = isDisjoint;
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


}