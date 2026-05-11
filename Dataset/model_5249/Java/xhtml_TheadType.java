





import java.util.List;
import java.util.ArrayList;

public class xhtml_TheadType  {

    private String align;
    private String style;
    private String class_;
    private String id;
    private String title;
    private String charoff;
    private String char;
    private String valign;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_TrType> xhtml_trtypes;


    public xhtml_TheadType(
        String align,        String style,        String class_,        String id,        String title,        String charoff,        String char,        String valign    ) {
        this.align = align;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.title = title;
        this.charoff = charoff;
        this.char = char;
        this.valign = valign;
        this.xhtml_trtypes = new ArrayList<>();
    }

    public xhtml_TheadType(
        String align,        String style,        String class_,        String id,        String title,        String charoff,        String char,        String valign        ArrayList<xhtml_TrType> xhtml_trtypes    ) {
        this.align = align;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.title = title;
        this.charoff = charoff;
        this.char = char;
        this.valign = valign;
        this.xhtml_trtypes = xhtml_trtypes;
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
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
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
    public List<xhtml_TrType> getXhtml_trtypes() {
        return xhtml_trtypes;
    }

    public void addXhtml_trtype(Xhtml_trtype xhtml_trtype) {
        this.xhtml_trtypes.add(xhtml_trtype);
    }

}