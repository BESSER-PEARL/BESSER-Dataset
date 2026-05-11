





import java.util.List;
import java.util.ArrayList;

public class slolpBPM_Type  {

    private String name;





    private slolpBPM_DomainModel slolpbpm_domainmodel;


    public slolpBPM_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public slolpBPM_DomainModel getSlolpbpm_domainmodel() {
        return slolpbpm_domainmodel;
    }

    public void setSlolpbpm_domainmodel(slolpBPM_DomainModel slolpbpm_domainmodel) {
        this.slolpbpm_domainmodel = slolpbpm_domainmodel;
    }

}