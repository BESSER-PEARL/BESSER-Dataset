





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_FeatureChangeListener  {

    private String domainClass;
    private String featureName;



    public viewpoint_tool_FeatureChangeListener(
        String domainClass,        String featureName    ) {
        this.domainClass = domainClass;
        this.featureName = featureName;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}