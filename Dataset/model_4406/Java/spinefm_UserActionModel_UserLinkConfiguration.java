





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserLinkConfiguration extends UserAction {

    private String assoName;
    private String confSourceName;
    private String confTargetName;



    public spinefm_UserActionModel_UserLinkConfiguration(
        String assoName,        String confSourceName,        String confTargetName    ) {
        super(
        );
        this.assoName = assoName;
        this.confSourceName = confSourceName;
        this.confTargetName = confTargetName;
    }


    public String getAssoname() {
        return assoName;
    }

    public void setAssoname(String assoName) {
        this.assoName = assoName;
    }
    public String getConfsourcename() {
        return confSourceName;
    }

    public void setConfsourcename(String confSourceName) {
        this.confSourceName = confSourceName;
    }
    public String getConftargetname() {
        return confTargetName;
    }

    public void setConftargetname(String confTargetName) {
        this.confTargetName = confTargetName;
    }


}