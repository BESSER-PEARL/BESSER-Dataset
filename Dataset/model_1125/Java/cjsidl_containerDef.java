





import java.util.List;
import java.util.ArrayList;

public class cjsidl_containerDef  {

    private String comment;
    private String optional;
    private String name;





    private cjsidl_listDef cjsidl_listdef;


    public cjsidl_containerDef(
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

    public cjsidl_listDef getCjsidl_listdef() {
        return cjsidl_listdef;
    }

    public void setCjsidl_listdef(cjsidl_listDef cjsidl_listdef) {
        this.cjsidl_listdef = cjsidl_listdef;
    }

}