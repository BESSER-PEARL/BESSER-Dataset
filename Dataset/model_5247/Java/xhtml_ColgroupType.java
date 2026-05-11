





import java.util.List;
import java.util.ArrayList;

public class xhtml_ColgroupType  {

    private String align;
    private String width;
    private String valign;
    private String char;
    private String id;
    private String charoff;
    private String title;
    private String span;
    private String style;
    private String class_;





    private xhtml_TableType xhtml_tabletype;


    public xhtml_ColgroupType(
        String align,        String width,        String valign,        String char,        String id,        String charoff,        String title,        String span,        String style,        String class_    ) {
        this.align = align;
        this.width = width;
        this.valign = valign;
        this.char = char;
        this.id = id;
        this.charoff = charoff;
        this.title = title;
        this.span = span;
        this.style = style;
        this.class_ = class_;
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
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
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

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}