





import java.util.List;
import java.util.ArrayList;

public class cjsidl_footerRef  {

    private String comment;
    private String name;





    private cjsidl_footerDef cjsidl_footerdef;


    public cjsidl_footerRef(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
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

    public cjsidl_footerDef getCjsidl_footerdef() {
        return cjsidl_footerdef;
    }

    public void setCjsidl_footerdef(cjsidl_footerDef cjsidl_footerdef) {
        this.cjsidl_footerdef = cjsidl_footerdef;
    }

}