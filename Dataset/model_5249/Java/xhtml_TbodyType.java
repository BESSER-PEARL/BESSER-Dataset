





import java.util.List;
import java.util.ArrayList;

public class xhtml_TbodyType  {

    private String class_;
    private String id;
    private String align;
    private String char;
    private String charoff;
    private String valign;
    private String title;
    private String style;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_TrType> xhtml_trtypes;


    public xhtml_TbodyType(
        String class_,        String id,        String align,        String char,        String charoff,        String valign,        String title,        String style    ) {
        this.class_ = class_;
        this.id = id;
        this.align = align;
        this.char = char;
        this.charoff = charoff;
        this.valign = valign;
        this.title = title;
        this.style = style;
        this.xhtml_trtypes = new ArrayList<>();
    }

    public xhtml_TbodyType(
        String class_,        String id,        String align,        String char,        String charoff,        String valign,        String title,        String style        ArrayList<xhtml_TrType> xhtml_trtypes    ) {
        this.class_ = class_;
        this.id = id;
        this.align = align;
        this.char = char;
        this.charoff = charoff;
        this.valign = valign;
        this.title = title;
        this.style = style;
        this.xhtml_trtypes = xhtml_trtypes;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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