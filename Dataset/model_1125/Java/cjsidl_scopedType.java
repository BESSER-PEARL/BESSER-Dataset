





import java.util.List;
import java.util.ArrayList;

public class cjsidl_scopedType  {






    private cjsidl_arrayDef cjsidl_arraydef;




    private cjsidl_containerRef cjsidl_containerref;




    private cjsidl_EObject cjsidl_eobject;




    private List<cjsidl_EObject> cjsidl_eobjects;




    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_scopedTypeId cjsidl_scopedtypeid;


    public cjsidl_scopedType(
    ) {
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_scopedType(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
    }


    public cjsidl_arrayDef getCjsidl_arraydef() {
        return cjsidl_arraydef;
    }

    public void setCjsidl_arraydef(cjsidl_arrayDef cjsidl_arraydef) {
        this.cjsidl_arraydef = cjsidl_arraydef;
    }
    public cjsidl_containerRef getCjsidl_containerref() {
        return cjsidl_containerref;
    }

    public void setCjsidl_containerref(cjsidl_containerRef cjsidl_containerref) {
        this.cjsidl_containerref = cjsidl_containerref;
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
    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_scopedTypeId getCjsidl_scopedtypeid() {
        return cjsidl_scopedtypeid;
    }

    public void setCjsidl_scopedtypeid(cjsidl_scopedTypeId cjsidl_scopedtypeid) {
        this.cjsidl_scopedtypeid = cjsidl_scopedtypeid;
    }

}