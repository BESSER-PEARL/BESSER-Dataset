





import java.util.List;
import java.util.ArrayList;

public class cjsidl_footerScopedRef  {






    private cjsidl_footerDef cjsidl_footerdef;




    private cjsidl_footerRef cjsidl_footerref;




    private cjsidl_EObject cjsidl_eobject;




    private List<cjsidl_EObject> cjsidl_eobjects;


    public cjsidl_footerScopedRef(
    ) {
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_footerScopedRef(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
    }


    public cjsidl_footerDef getCjsidl_footerdef() {
        return cjsidl_footerdef;
    }

    public void setCjsidl_footerdef(cjsidl_footerDef cjsidl_footerdef) {
        this.cjsidl_footerdef = cjsidl_footerdef;
    }
    public cjsidl_footerRef getCjsidl_footerref() {
        return cjsidl_footerref;
    }

    public void setCjsidl_footerref(cjsidl_footerRef cjsidl_footerref) {
        this.cjsidl_footerref = cjsidl_footerref;
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

}