





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_Type  {

    private String name;





    private giraffeDSL_DomainModel giraffedsl_domainmodel;


    public giraffeDSL_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public giraffeDSL_DomainModel getGiraffedsl_domainmodel() {
        return giraffedsl_domainmodel;
    }

    public void setGiraffedsl_domainmodel(giraffeDSL_DomainModel giraffedsl_domainmodel) {
        this.giraffedsl_domainmodel = giraffedsl_domainmodel;
    }

}