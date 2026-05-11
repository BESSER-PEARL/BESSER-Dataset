





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Type  {

    private String name;





    private domainmodel_Domainmodel domainmodel_domainmodel;


    public domainmodel_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_Domainmodel getDomainmodel_domainmodel() {
        return domainmodel_domainmodel;
    }

    public void setDomainmodel_domainmodel(domainmodel_Domainmodel domainmodel_domainmodel) {
        this.domainmodel_domainmodel = domainmodel_domainmodel;
    }

}