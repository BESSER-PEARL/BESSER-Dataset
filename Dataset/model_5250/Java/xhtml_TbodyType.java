





import java.util.List;
import java.util.ArrayList;

public class xhtml_TbodyType  {

    private String valign;
    private String char;
    private String id;
    private String style;
    private String align;
    private String class_;
    private String title;
    private String charoff;





    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_TrType> xhtml_trtypes;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TbodyType(
        String valign,        String char,        String id,        String style,        String align,        String class_,        String title,        String charoff    ) {
        this.valign = valign;
        this.char = char;
        this.id = id;
        this.style = style;
        this.align = align;
        this.class_ = class_;
        this.title = title;
        this.charoff = charoff;
        this.xhtml_trtypes = new ArrayList<>();
    }

    public xhtml_TbodyType(
        String valign,        String char,        String id,        String style,        String align,        String class_,        String title,        String charoff        ArrayList<xhtml_TrType> xhtml_trtypes    ) {
        this.valign = valign;
        this.char = char;
        this.id = id;
        this.style = style;
        this.align = align;
        this.class_ = class_;
        this.title = title;
        this.charoff = charoff;
        this.xhtml_trtypes = xhtml_trtypes;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}