





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserDeselect extends UserAction {

    private String domainElementName;
    private String contextID;
    private String featureName;



    public spinefm_UserActionModel_UserDeselect(
        String domainElementName,        String contextID,        String featureName    ) {
        super(
        );
        this.domainElementName = domainElementName;
        this.contextID = contextID;
        this.featureName = featureName;
    }


    public String getDomainelementname() {
        return domainElementName;
    }

    public void setDomainelementname(String domainElementName) {
        this.domainElementName = domainElementName;
    }
    public String getContextid() {
        return contextID;
    }

    public void setContextid(String contextID) {
        this.contextID = contextID;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}