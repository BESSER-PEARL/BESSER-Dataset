





import java.util.List;
import java.util.ArrayList;

public class xhtml_TfootType  {

    private String style;
    private String char;
    private String align;
    private String charoff;
    private String title;
    private String class_;
    private String id;
    private String valign;





    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TfootType(
        String style,        String char,        String align,        String charoff,        String title,        String class_,        String id,        String valign    ) {
        this.style = style;
        this.char = char;
        this.align = align;
        this.charoff = charoff;
        this.title = title;
        this.class_ = class_;
        this.id = id;
        this.valign = valign;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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