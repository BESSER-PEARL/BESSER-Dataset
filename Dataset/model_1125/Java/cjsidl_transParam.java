





import java.util.List;
import java.util.ArrayList;

public class cjsidl_transParam  {

    private String comment;
    private String name;
    private String unsignedType;





    private cjsidl_transParams cjsidl_transparams;




    private cjsidl_EObject cjsidl_eobject;


    public cjsidl_transParam(
        String comment,        String name,        String unsignedType    ) {
        this.comment = comment;
        this.name = name;
        this.unsignedType = unsignedType;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnsignedtype() {
        return unsignedType;
    }

    public void setUnsignedtype(String unsignedType) {
        this.unsignedType = unsignedType;
    }

    public cjsidl_transParams getCjsidl_transparams() {
        return cjsidl_transparams;
    }

    public void setCjsidl_transparams(cjsidl_transParams cjsidl_transparams) {
        this.cjsidl_transparams = cjsidl_transparams;
    }
    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }

}