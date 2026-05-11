





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserValidConfiguration extends UserAction {

    private String contextID;
    private String domainElementName;



    public spinefm_UserActionModel_UserValidConfiguration(
        String contextID,        String domainElementName    ) {
        super(
        );
        this.contextID = contextID;
        this.domainElementName = domainElementName;
    }


    public String getContextid() {
        return contextID;
    }

    public void setContextid(String contextID) {
        this.contextID = contextID;
    }
    public String getDomainelementname() {
        return domainElementName;
    }

    public void setDomainelementname(String domainElementName) {
        this.domainElementName = domainElementName;
    }


}