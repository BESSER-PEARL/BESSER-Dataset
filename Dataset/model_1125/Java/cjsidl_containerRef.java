





import java.util.List;
import java.util.ArrayList;

public class cjsidl_containerRef  {

    private String comment;
    private String name;
    private String optional;





    private cjsidl_listDef cjsidl_listdef;




    private cjsidl_containerDef cjsidl_containerdef;


    public cjsidl_containerRef(
        String comment,        String name,        String optional    ) {
        this.comment = comment;
        this.name = name;
        this.optional = optional;
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
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }

    public cjsidl_listDef getCjsidl_listdef() {
        return cjsidl_listdef;
    }

    public void setCjsidl_listdef(cjsidl_listDef cjsidl_listdef) {
        this.cjsidl_listdef = cjsidl_listdef;
    }
    public cjsidl_containerDef getCjsidl_containerdef() {
        return cjsidl_containerdef;
    }

    public void setCjsidl_containerdef(cjsidl_containerDef cjsidl_containerdef) {
        this.cjsidl_containerdef = cjsidl_containerdef;
    }

}