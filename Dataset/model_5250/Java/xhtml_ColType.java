





import java.util.List;
import java.util.ArrayList;

public class xhtml_ColType  {

    private String valign;
    private String charoff;
    private String style;
    private String width;
    private String align;
    private String char;
    private String id;
    private String title;
    private String class_;
    private String span;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_ColgroupType xhtml_colgrouptype;


    public xhtml_ColType(
        String valign,        String charoff,        String style,        String width,        String align,        String char,        String id,        String title,        String class_,        String span    ) {
        this.valign = valign;
        this.charoff = charoff;
        this.style = style;
        this.width = width;
        this.align = align;
        this.char = char;
        this.id = id;
        this.title = title;
        this.class_ = class_;
        this.span = span;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }
    public xhtml_ColgroupType getXhtml_colgrouptype() {
        return xhtml_colgrouptype;
    }

    public void setXhtml_colgrouptype(xhtml_ColgroupType xhtml_colgrouptype) {
        this.xhtml_colgrouptype = xhtml_colgrouptype;
    }

}