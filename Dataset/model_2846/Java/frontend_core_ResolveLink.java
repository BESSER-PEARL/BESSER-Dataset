





import java.util.List;
import java.util.ArrayList;

public class frontend_core_ResolveLink extends Expression {

    private String featureName;
    private String linkName;
    private String isExternal;



    public frontend_core_ResolveLink(
        String featureName,        String linkName,        String isExternal    ) {
        super(
        );
        this.featureName = featureName;
        this.linkName = linkName;
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
    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }


}