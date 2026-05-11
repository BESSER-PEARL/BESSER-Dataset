





import java.util.List;
import java.util.ArrayList;

public class core_ResolveLink extends Expression {

    private String linkName;
    private String isExternal;
    private String featureName;





    private core_UseDeclaration core_usedeclaration;


    public core_ResolveLink(
        String linkName,        String isExternal,        String featureName    ) {
        super(
        );
        this.linkName = linkName;
        this.isExternal = isExternal;
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
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }

    public core_UseDeclaration getCore_usedeclaration() {
        return core_usedeclaration;
    }

    public void setCore_usedeclaration(core_UseDeclaration core_usedeclaration) {
        this.core_usedeclaration = core_usedeclaration;
    }

}