





import java.util.List;
import java.util.ArrayList;

public class cjsidl_arrayDef  {

    private String name;
    private String comment;
    private String arraySize;
    private String optional;





    private cjsidl_typeDef cjsidl_typedef;




    private cjsidl_EObject cjsidl_eobject;


    public cjsidl_arrayDef(
        String name,        String comment,        String arraySize,        String optional    ) {
        this.name = name;
        this.comment = comment;
        this.arraySize = arraySize;
        this.optional = optional;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getArraysize() {
        return arraySize;
    }

    public void setArraysize(String arraySize) {
        this.arraySize = arraySize;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }

}