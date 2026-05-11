





import java.util.List;
import java.util.ArrayList;

public class xhtml_TbodyType  {

    private String charoff;
    private String align;
    private String valign;
    private String id;
    private String char;
    private String class_;
    private String style;
    private String title;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_DocumentRoot xhtml_documentroot;


    public xhtml_TbodyType(
        String charoff,        String align,        String valign,        String id,        String char,        String class_,        String style,        String title    ) {
        this.charoff = charoff;
        this.align = align;
        this.valign = valign;
        this.id = id;
        this.char = char;
        this.class_ = class_;
        this.style = style;
        this.title = title;
    }


    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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