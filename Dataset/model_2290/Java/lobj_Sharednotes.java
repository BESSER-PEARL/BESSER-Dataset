





import java.util.List;
import java.util.ArrayList;

public class lobj_Sharednotes  {

    private String id;





    private lobj_AccessControl lobj_accesscontrol;


    public lobj_Sharednotes(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }

}