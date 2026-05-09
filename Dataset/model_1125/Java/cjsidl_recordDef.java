





import java.util.List;
import java.util.ArrayList;

public class cjsidl_recordDef extends containerDef {






    private cjsidl_typeDef cjsidl_typedef;




    private List<cjsidl_typeReference> cjsidl_typereferences;




    private List<cjsidl_arrayDef> cjsidl_arraydefs;




    private List<cjsidl_scopedTypeId> cjsidl_scopedtypeids;


    public cjsidl_recordDef(
    ) {
        super(
        );
        this.cjsidl_typereferences = new ArrayList<>();
        this.cjsidl_arraydefs = new ArrayList<>();
        this.cjsidl_scopedtypeids = new ArrayList<>();
    }

    public cjsidl_recordDef(
        ArrayList<cjsidl_typeReference> cjsidl_typereferences,        ArrayList<cjsidl_arrayDef> cjsidl_arraydefs,        ArrayList<cjsidl_scopedTypeId> cjsidl_scopedtypeids    ) {
        this.cjsidl_typereferences = cjsidl_typereferences;
        this.cjsidl_arraydefs = cjsidl_arraydefs;
        this.cjsidl_scopedtypeids = cjsidl_scopedtypeids;
    }


    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public List<cjsidl_typeReference> getCjsidl_typereferences() {
        return cjsidl_typereferences;
    }

    public void addCjsidl_typereference(Cjsidl_typereference cjsidl_typereference) {
        this.cjsidl_typereferences.add(cjsidl_typereference);
    }
    public List<cjsidl_arrayDef> getCjsidl_arraydefs() {
        return cjsidl_arraydefs;
    }

    public void addCjsidl_arraydef(Cjsidl_arraydef cjsidl_arraydef) {
        this.cjsidl_arraydefs.add(cjsidl_arraydef);
    }
    public List<cjsidl_scopedTypeId> getCjsidl_scopedtypeids() {
        return cjsidl_scopedtypeids;
    }

    public void addCjsidl_scopedtypeid(Cjsidl_scopedtypeid cjsidl_scopedtypeid) {
        this.cjsidl_scopedtypeids.add(cjsidl_scopedtypeid);
    }

}