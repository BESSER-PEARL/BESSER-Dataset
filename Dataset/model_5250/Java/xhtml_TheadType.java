





import java.util.List;
import java.util.ArrayList;

public class xhtml_TheadType  {

    private String char;
    private String class_;
    private String align;
    private String style;
    private String id;
    private String title;
    private String valign;
    private String charoff;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_DocumentRoot xhtml_documentroot;


    public xhtml_TheadType(
        String char,        String class_,        String align,        String style,        String id,        String title,        String valign,        String charoff    ) {
        this.char = char;
        this.class_ = class_;
        this.align = align;
        this.style = style;
        this.id = id;
        this.title = title;
        this.valign = valign;
        this.charoff = charoff;
    }


    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }

}