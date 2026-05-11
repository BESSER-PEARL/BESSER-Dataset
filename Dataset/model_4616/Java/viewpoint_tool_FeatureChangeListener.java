





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_FeatureChangeListener  {

    private String featureName;
    private String domainClass;



    public viewpoint_tool_FeatureChangeListener(
        String featureName,        String domainClass    ) {
        this.featureName = featureName;
        this.domainClass = domainClass;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }


}