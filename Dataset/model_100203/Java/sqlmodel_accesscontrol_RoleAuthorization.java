





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_accesscontrol_RoleAuthorization extends SQLObject {

    private boolean grantable;



    public sqlmodel_accesscontrol_RoleAuthorization(
        boolean grantable    ) {
        super(
        );
        this.grantable = grantable;
    }


    public boolean getGrantable() {
        return grantable;
    }

    public void setGrantable(boolean grantable) {
        this.grantable = grantable;
    }


}