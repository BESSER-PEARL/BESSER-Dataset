





import java.util.List;
import java.util.ArrayList;

public class xhtml_BlockquoteType extends Block {

    private String cite;
    private String style;
    private String class_;
    private String id;
    private String title;





    private xhtml_Block xhtml_block;




    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_BlockquoteType(
        String cite,        String style,        String class_,        String id,        String title    ) {
        super(
        );
        this.cite = cite;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.title = title;
    }


    public String getCite() {
        return cite;
    }

    public void setCite(String cite) {
        this.cite = cite;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}