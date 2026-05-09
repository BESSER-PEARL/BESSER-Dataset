





import java.util.List;
import java.util.ArrayList;

public class cjsidl_scopedEventType  {






    private cjsidl_transParam cjsidl_transparam;




    private cjsidl_EObject cjsidl_eobject;




    private List<cjsidl_EObject> cjsidl_eobjects;




    private cjsidl_EObject cjsidl_eobject;


    public cjsidl_scopedEventType(
    ) {
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_scopedEventType(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
    }


    public cjsidl_transParam getCjsidl_transparam() {
        return cjsidl_transparam;
    }

    public void setCjsidl_transparam(cjsidl_transParam cjsidl_transparam) {
        this.cjsidl_transparam = cjsidl_transparam;
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

}