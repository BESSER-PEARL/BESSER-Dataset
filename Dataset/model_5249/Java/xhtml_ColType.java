





import java.util.List;
import java.util.ArrayList;

public class xhtml_ColType  {

    private String char;
    private String valign;
    private String charoff;
    private String span;
    private String align;
    private String width;
    private String id;
    private String title;
    private String class_;
    private String style;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_ColgroupType xhtml_colgrouptype;


    public xhtml_ColType(
        String char,        String valign,        String charoff,        String span,        String align,        String width,        String id,        String title,        String class_,        String style    ) {
        this.char = char;
        this.valign = valign;
        this.charoff = charoff;
        this.span = span;
        this.align = align;
        this.width = width;
        this.id = id;
        this.title = title;
        this.class_ = class_;
        this.style = style;
    }


    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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