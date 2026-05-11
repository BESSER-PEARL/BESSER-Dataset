





import java.util.List;
import java.util.ArrayList;

public class lobj_Userauthorization  {

    private String id;





    private lobj_User lobj_user;




    private lobj_AccessControl lobj_accesscontrol;


    public lobj_Userauthorization(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_User getLobj_user() {
        return lobj_user;
    }

    public void setLobj_user(lobj_User lobj_user) {
        this.lobj_user = lobj_user;
    }
    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }

}