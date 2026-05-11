





import java.util.List;
import java.util.ArrayList;

public class xhtml_TheadType  {

    private String style;
    private String charoff;
    private String valign;
    private String id;
    private String class_;
    private String align;
    private String char;
    private String title;





    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TheadType(
        String style,        String charoff,        String valign,        String id,        String class_,        String align,        String char,        String title    ) {
        this.style = style;
        this.charoff = charoff;
        this.valign = valign;
        this.id = id;
        this.class_ = class_;
        this.align = align;
        this.char = char;
        this.title = title;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}