





import java.util.List;
import java.util.ArrayList;

public class lobj_AuthorizationTypes  {

    private boolean readOnly;
    private String id;
    private String authTypeDesc;
    private String authType;





    private lobj_Userauthorization lobj_userauthorization;




    private lobj_User lobj_user;


    public lobj_AuthorizationTypes(
        boolean readOnly,        String id,        String authTypeDesc,        String authType    ) {
        this.readOnly = readOnly;
        this.id = id;
        this.authTypeDesc = authTypeDesc;
        this.authType = authType;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAuthtypedesc() {
        return authTypeDesc;
    }

    public void setAuthtypedesc(String authTypeDesc) {
        this.authTypeDesc = authTypeDesc;
    }
    public String getAuthtype() {
        return authType;
    }

    public void setAuthtype(String authType) {
        this.authType = authType;
    }

    public lobj_Userauthorization getLobj_userauthorization() {
        return lobj_userauthorization;
    }

    public void setLobj_userauthorization(lobj_Userauthorization lobj_userauthorization) {
        this.lobj_userauthorization = lobj_userauthorization;
    }
    public lobj_User getLobj_user() {
        return lobj_user;
    }

    public void setLobj_user(lobj_User lobj_user) {
        this.lobj_user = lobj_user;
    }

}