





import java.util.List;
import java.util.ArrayList;

public class cjsidl_action  {

    private String comment;
    private String name;





    private cjsidl_sendActionList cjsidl_sendactionlist;




    private List<cjsidl_guardParam> cjsidl_guardparams;




    private cjsidl_actionList cjsidl_actionlist;


    public cjsidl_action(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
        this.cjsidl_guardparams = new ArrayList<>();
    }

    public cjsidl_action(
        String comment,        String name        ArrayList<cjsidl_guardParam> cjsidl_guardparams    ) {
        this.comment = comment;
        this.name = name;
        this.cjsidl_guardparams = cjsidl_guardparams;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_sendActionList getCjsidl_sendactionlist() {
        return cjsidl_sendactionlist;
    }

    public void setCjsidl_sendactionlist(cjsidl_sendActionList cjsidl_sendactionlist) {
        this.cjsidl_sendactionlist = cjsidl_sendactionlist;
    }
    public List<cjsidl_guardParam> getCjsidl_guardparams() {
        return cjsidl_guardparams;
    }

    public void addCjsidl_guardparam(Cjsidl_guardparam cjsidl_guardparam) {
        this.cjsidl_guardparams.add(cjsidl_guardparam);
    }
    public cjsidl_actionList getCjsidl_actionlist() {
        return cjsidl_actionlist;
    }

    public void setCjsidl_actionlist(cjsidl_actionList cjsidl_actionlist) {
        this.cjsidl_actionlist = cjsidl_actionlist;
    }

}