





import java.util.List;
import java.util.ArrayList;

public class cjsidl_sequenceDef extends containerDef {






    private cjsidl_typeDef cjsidl_typedef;




    private List<cjsidl_EObject> cjsidl_eobjects;


    public cjsidl_sequenceDef(
    ) {
        super(
        );
        this.cjsidl_eobjects = new ArrayList<>();
    }

    public cjsidl_sequenceDef(
        ArrayList<cjsidl_EObject> cjsidl_eobjects    ) {
        this.cjsidl_eobjects = cjsidl_eobjects;
    }


    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public List<cjsidl_EObject> getCjsidl_eobjects() {
        return cjsidl_eobjects;
    }

    public void addCjsidl_eobject(Cjsidl_eobject cjsidl_eobject) {
        this.cjsidl_eobjects.add(cjsidl_eobject);
    }

}