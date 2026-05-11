





import java.util.List;
import java.util.ArrayList;

public class domainmodel_MainFeatureOption  {

    private String name;





    private domainmodel_MainFeature domainmodel_mainfeature;


    public domainmodel_MainFeatureOption(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_MainFeature getDomainmodel_mainfeature() {
        return domainmodel_mainfeature;
    }

    public void setDomainmodel_mainfeature(domainmodel_MainFeature domainmodel_mainfeature) {
        this.domainmodel_mainfeature = domainmodel_mainfeature;
    }

}