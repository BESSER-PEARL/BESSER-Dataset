





import java.util.List;
import java.util.ArrayList;

public class cjsidl_varField  {

    private String optional;
    private String name;
    private String comment;





    private cjsidl_recordDef cjsidl_recorddef;




    private cjsidl_typeDef cjsidl_typedef;


    public cjsidl_varField(
        String optional,        String name,        String comment    ) {
        this.optional = optional;
        this.name = name;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_recordDef getCjsidl_recorddef() {
        return cjsidl_recorddef;
    }

    public void setCjsidl_recorddef(cjsidl_recordDef cjsidl_recorddef) {
        this.cjsidl_recorddef = cjsidl_recorddef;
    }
    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }

}