





import java.util.List;
import java.util.ArrayList;

public class xhtml_BrType  {

    private String class_;
    private String title;
    private String style;
    private String id;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_AContent xhtml_acontent;


    public xhtml_BrType(
        String class_,        String title,        String style,        String id    ) {
        this.class_ = class_;
        this.title = title;
        this.style = style;
        this.id = id;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }

}