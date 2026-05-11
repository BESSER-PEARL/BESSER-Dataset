





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserSelect extends UserAction {

    private String domainElementName;
    private String featureName;
    private String contextID;



    public spinefm_UserActionModel_UserSelect(
        String domainElementName,        String featureName,        String contextID    ) {
        super(
        );
        this.domainElementName = domainElementName;
        this.featureName = featureName;
        this.contextID = contextID;
    }


    public String getDomainelementname() {
        return domainElementName;
    }

    public void setDomainelementname(String domainElementName) {
        this.domainElementName = domainElementName;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getContextid() {
        return contextID;
    }

    public void setContextid(String contextID) {
        this.contextID = contextID;
    }


}