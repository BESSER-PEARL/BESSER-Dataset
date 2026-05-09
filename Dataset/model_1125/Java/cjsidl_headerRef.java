





import java.util.List;
import java.util.ArrayList;

public class cjsidl_headerRef  {

    private String comment;
    private String name;





    private cjsidl_headerDef cjsidl_headerdef;


    public cjsidl_headerRef(
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

    public cjsidl_headerDef getCjsidl_headerdef() {
        return cjsidl_headerdef;
    }

    public void setCjsidl_headerdef(cjsidl_headerDef cjsidl_headerdef) {
        this.cjsidl_headerdef = cjsidl_headerdef;
    }

}