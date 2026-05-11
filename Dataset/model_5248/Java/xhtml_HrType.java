





import java.util.List;
import java.util.ArrayList;

public class xhtml_HrType  {

    private String title;
    private String class_;
    private String id;
    private String style;





    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_HrType(
        String title,        String class_,        String id,        String style    ) {
        this.title = title;
        this.class_ = class_;
        this.id = id;
        this.style = style;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}