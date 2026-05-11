





import java.util.List;
import java.util.ArrayList;

public class xhtml_HtmlType  {

    private String id;





    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_BodyType xhtml_bodytype;


    public xhtml_HtmlType(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_BodyType getXhtml_bodytype() {
        return xhtml_bodytype;
    }

    public void setXhtml_bodytype(xhtml_BodyType xhtml_bodytype) {
        this.xhtml_bodytype = xhtml_bodytype;
    }

}