





import java.util.List;
import java.util.ArrayList;

public class xhtml_BlockquoteType extends Block {

    private String style;
    private String id;
    private String title;
    private String class_;
    private String cite;





    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_BlockquoteType(
        String style,        String id,        String title,        String class_,        String cite    ) {
        super(
        );
        this.style = style;
        this.id = id;
        this.title = title;
        this.class_ = class_;
        this.cite = cite;
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
    public String getCite() {
        return cite;
    }

    public void setCite(String cite) {
        this.cite = cite;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}