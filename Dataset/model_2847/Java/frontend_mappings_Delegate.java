





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Delegate extends LocatedElement {

    private String isExternal;
    private String featureName;
    private String linkName;



    public frontend_mappings_Delegate(
        String isExternal,        String featureName,        String linkName    ) {
        super(
        );
        this.isExternal = isExternal;
        this.featureName = featureName;
        this.linkName = linkName;
    }


    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getLinkname() {
        return linkName;
    }

    public void setLinkname(String linkName) {
        this.linkName = linkName;
    }


}