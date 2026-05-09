





import java.util.List;
import java.util.ArrayList;

public class cjsidl_scopedTypeId  {

    private String scopedName;
    private String comment;
    private String optional;





    private cjsidl_declaredTypeSet cjsidl_declaredtypeset;


    public cjsidl_scopedTypeId(
        String scopedName,        String comment,        String optional    ) {
        this.scopedName = scopedName;
        this.comment = comment;
        this.optional = optional;
    }


    public String getScopedname() {
        return scopedName;
    }

    public void setScopedname(String scopedName) {
        this.scopedName = scopedName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }

    public cjsidl_declaredTypeSet getCjsidl_declaredtypeset() {
        return cjsidl_declaredtypeset;
    }

    public void setCjsidl_declaredtypeset(cjsidl_declaredTypeSet cjsidl_declaredtypeset) {
        this.cjsidl_declaredtypeset = cjsidl_declaredtypeset;
    }

}