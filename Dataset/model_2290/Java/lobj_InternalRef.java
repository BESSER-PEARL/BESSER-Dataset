





import java.util.List;
import java.util.ArrayList;

public class lobj_InternalRef  {

    private String reftype;
    private String file;
    private String id;
    private String ref;





    private lobj_Language lobj_language;




    private lobj_Precognition lobj_precognition;


    public lobj_InternalRef(
        String reftype,        String file,        String id,        String ref    ) {
        this.reftype = reftype;
        this.file = file;
        this.id = id;
        this.ref = ref;
    }


    public String getReftype() {
        return reftype;
    }

    public void setReftype(String reftype) {
        this.reftype = reftype;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }
    public lobj_Precognition getLobj_precognition() {
        return lobj_precognition;
    }

    public void setLobj_precognition(lobj_Precognition lobj_precognition) {
        this.lobj_precognition = lobj_precognition;
    }

}