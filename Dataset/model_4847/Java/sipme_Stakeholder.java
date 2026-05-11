





import java.util.List;
import java.util.ArrayList;

public class sipme_Stakeholder extends SIPME_object {

    private String stakeholderOrganism;
    private String stakeholderType;



    public sipme_Stakeholder(
        String stakeholderOrganism,        String stakeholderType    ) {
        super(
        );
        this.stakeholderOrganism = stakeholderOrganism;
        this.stakeholderType = stakeholderType;
    }


    public String getStakeholderorganism() {
        return stakeholderOrganism;
    }

    public void setStakeholderorganism(String stakeholderOrganism) {
        this.stakeholderOrganism = stakeholderOrganism;
    }
    public String getStakeholdertype() {
        return stakeholderType;
    }

    public void setStakeholdertype(String stakeholderType) {
        this.stakeholderType = stakeholderType;
    }


}