





import java.util.List;
import java.util.ArrayList;

public class cjsidl_bodyScopedRef  {






    private cjsidl_EObject cjsidl_eobject;




    private List<cjsidl_EObject> cjsidl_eobjects;




    private cjsidl_bodyDef cjsidl_bodydef;




    private cjsidl_bodyRef cjsidl_bodyref;


    public cjsidl_bodyScopedRef(
    ) {
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_bodyScopedRef(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
    }


    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public List<cjsidl_EObject> getCjsidl_eobjects() {
        return cjsidl_eobjects;
    }

    public void addCjsidl_eobject(Cjsidl_eobject cjsidl_eobject) {
        this.cjsidl_eobjects.add(cjsidl_eobject);
    }
    public cjsidl_bodyDef getCjsidl_bodydef() {
        return cjsidl_bodydef;
    }

    public void setCjsidl_bodydef(cjsidl_bodyDef cjsidl_bodydef) {
        this.cjsidl_bodydef = cjsidl_bodydef;
    }
    public cjsidl_bodyRef getCjsidl_bodyref() {
        return cjsidl_bodyref;
    }

    public void setCjsidl_bodyref(cjsidl_bodyRef cjsidl_bodyref) {
        this.cjsidl_bodyref = cjsidl_bodyref;
    }

}