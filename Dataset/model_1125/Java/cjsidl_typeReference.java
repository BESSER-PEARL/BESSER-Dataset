





import java.util.List;
import java.util.ArrayList;

public class cjsidl_typeReference  {

    private String comment;
    private String optional;
    private String name;





    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_declaredTypeSet cjsidl_declaredtypeset;


    public cjsidl_typeReference(
        String comment,        String optional,        String name    ) {
        this.comment = comment;
        this.optional = optional;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_declaredTypeSet getCjsidl_declaredtypeset() {
        return cjsidl_declaredtypeset;
    }

    public void setCjsidl_declaredtypeset(cjsidl_declaredTypeSet cjsidl_declaredtypeset) {
        this.cjsidl_declaredtypeset = cjsidl_declaredtypeset;
    }

}