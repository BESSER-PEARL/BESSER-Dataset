





import java.util.List;
import java.util.ArrayList;

public class xhtml_DivType extends Flow {

    private String style;
    private String id;
    private String class_;
    private String title;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_Block xhtml_block;


    public xhtml_DivType(
        String style,        String id,        String class_,        String title    ) {
        super(
        );
        this.style = style;
        this.id = id;
        this.class_ = class_;
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

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}