





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_accesscontrol_Privilege extends SQLObject {

    private String action;
    private boolean withHierarchy;
    private boolean grantable;



    public sqlmodel_accesscontrol_Privilege(
        String action,        boolean withHierarchy,        boolean grantable    ) {
        super(
        );
        this.action = action;
        this.withHierarchy = withHierarchy;
        this.grantable = grantable;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public boolean getWithhierarchy() {
        return withHierarchy;
    }

    public void setWithhierarchy(boolean withHierarchy) {
        this.withHierarchy = withHierarchy;
    }
    public boolean getGrantable() {
        return grantable;
    }

    public void setGrantable(boolean grantable) {
        this.grantable = grantable;
    }


}