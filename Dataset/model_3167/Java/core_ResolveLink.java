





import java.util.List;
import java.util.ArrayList;

public class core_ResolveLink extends Expression {

    private String linkName;
    private String featureName;
    private String isExternal;





    private core_UseDeclaration core_usedeclaration;




    private core_Expression core_expression;


    public core_ResolveLink(
        String linkName,        String featureName,        String isExternal    ) {
        super(
        );
        this.linkName = linkName;
        this.featureName = featureName;
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
    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }

    public core_UseDeclaration getCore_usedeclaration() {
        return core_usedeclaration;
    }

    public void setCore_usedeclaration(core_UseDeclaration core_usedeclaration) {
        this.core_usedeclaration = core_usedeclaration;
    }
    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }

}