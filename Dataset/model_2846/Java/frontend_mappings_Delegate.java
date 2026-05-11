





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Delegate extends LocatedElement {

    private String isExternal;
    private String linkName;
    private String featureName;



    public frontend_mappings_Delegate(
        String isExternal,        String linkName,        String featureName    ) {
        super(
        );
        this.isExternal = isExternal;
        this.linkName = linkName;
        this.featureName = featureName;
    }


    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }
    public String getLinkname() {
        return linkName;
    }

    public void setLinkname(String linkName) {
        this.linkName = linkName;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}