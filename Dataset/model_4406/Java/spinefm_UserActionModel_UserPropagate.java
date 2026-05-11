





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserPropagate extends UserAction {

    private String domainElementName;
    private String contextID;



    public spinefm_UserActionModel_UserPropagate(
        String domainElementName,        String contextID    ) {
        super(
        );
        this.domainElementName = domainElementName;
        this.contextID = contextID;
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


}