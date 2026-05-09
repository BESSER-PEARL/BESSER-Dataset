





import java.util.List;
import java.util.ArrayList;

public class cjsidl_bodyRef  {

    private String name;
    private String comment;





    private cjsidl_bodyDef cjsidl_bodydef;


    public cjsidl_bodyRef(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
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

    public cjsidl_bodyDef getCjsidl_bodydef() {
        return cjsidl_bodydef;
    }

    public void setCjsidl_bodydef(cjsidl_bodyDef cjsidl_bodydef) {
        this.cjsidl_bodydef = cjsidl_bodydef;
    }

}