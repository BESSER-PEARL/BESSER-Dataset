





import java.util.List;
import java.util.ArrayList;

public class dXP_UserId  {

    private String type;
    private String identifier;





    private dXP_User dxp_user;


    public dXP_UserId(
        String type,        String identifier    ) {
        this.type = type;
        this.identifier = identifier;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public dXP_User getDxp_user() {
        return dxp_user;
    }

    public void setDxp_user(dXP_User dxp_user) {
        this.dxp_user = dxp_user;
    }

}