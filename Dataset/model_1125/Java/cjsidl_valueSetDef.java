





import java.util.List;
import java.util.ArrayList;

public class cjsidl_valueSetDef  {

    private String offset;





    private List<cjsidl_EObject> cjsidl_eobjects;


    public cjsidl_valueSetDef(
        String offset    ) {
        this.offset = offset;
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_valueSetDef(
        String offset        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.offset = offset;
        this.cjsidl_eobjects = cjsidl_eobjects;
    }

    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }

    public List<cjsidl_EObject> getCjsidl_eobjects() {
        return cjsidl_eobjects;
    }

    public void addCjsidl_eobject(Cjsidl_eobject cjsidl_eobject) {
        this.cjsidl_eobjects.add(cjsidl_eobject);
    }

}