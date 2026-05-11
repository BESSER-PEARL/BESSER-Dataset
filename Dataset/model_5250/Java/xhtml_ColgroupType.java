





import java.util.List;
import java.util.ArrayList;

public class xhtml_ColgroupType  {

    private String class_;
    private String id;
    private String charoff;
    private String title;
    private String char;
    private String width;
    private String align;
    private String span;
    private String valign;
    private String style;





    private xhtml_TableType xhtml_tabletype;


    public xhtml_ColgroupType(
        String class_,        String id,        String charoff,        String title,        String char,        String width,        String align,        String span,        String valign,        String style    ) {
        this.class_ = class_;
        this.id = id;
        this.charoff = charoff;
        this.title = title;
        this.char = char;
        this.width = width;
        this.align = align;
        this.span = span;
        this.valign = valign;
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
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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

}