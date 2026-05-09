





import java.util.List;
import java.util.ArrayList;

public class cjsidl_transition  {

    private String comment;
    private String type;
    private String name;





    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_defaultState cjsidl_defaultstate;




    private cjsidl_state cjsidl_state;




    private List<cjsidl_refAttr> cjsidl_refattrs;


    public cjsidl_transition(
        String comment,        String type,        String name    ) {
        this.comment = comment;
        this.type = type;
        this.name = name;
        this.cjsidl_refattrs = new ArrayList<>();
    }

    public cjsidl_transition(
        String comment,        String type,        String name        ArrayList<cjsidl_refAttr> cjsidl_refattrs    ) {
        this.comment = comment;
        this.type = type;
        this.name = name;
        this.cjsidl_refattrs = cjsidl_refattrs;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_defaultState getCjsidl_defaultstate() {
        return cjsidl_defaultstate;
    }

    public void setCjsidl_defaultstate(cjsidl_defaultState cjsidl_defaultstate) {
        this.cjsidl_defaultstate = cjsidl_defaultstate;
    }
    public cjsidl_state getCjsidl_state() {
        return cjsidl_state;
    }

    public void setCjsidl_state(cjsidl_state cjsidl_state) {
        this.cjsidl_state = cjsidl_state;
    }
    public List<cjsidl_refAttr> getCjsidl_refattrs() {
        return cjsidl_refattrs;
    }

    public void addCjsidl_refattr(Cjsidl_refattr cjsidl_refattr) {
        this.cjsidl_refattrs.add(cjsidl_refattr);
    }

}