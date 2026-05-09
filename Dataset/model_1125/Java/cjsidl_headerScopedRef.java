





import java.util.List;
import java.util.ArrayList;

public class cjsidl_headerScopedRef  {






    private List<cjsidl_EObject> cjsidl_eobjects;




    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_headerDef cjsidl_headerdef;




    private cjsidl_headerRef cjsidl_headerref;


    public cjsidl_headerScopedRef(
    ) {
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_headerScopedRef(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
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
    public cjsidl_headerDef getCjsidl_headerdef() {
        return cjsidl_headerdef;
    }

    public void setCjsidl_headerdef(cjsidl_headerDef cjsidl_headerdef) {
        this.cjsidl_headerdef = cjsidl_headerdef;
    }
    public cjsidl_headerRef getCjsidl_headerref() {
        return cjsidl_headerref;
    }

    public void setCjsidl_headerref(cjsidl_headerRef cjsidl_headerref) {
        this.cjsidl_headerref = cjsidl_headerref;
    }

}