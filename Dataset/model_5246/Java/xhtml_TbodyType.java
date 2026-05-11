





import java.util.List;
import java.util.ArrayList;

public class xhtml_TbodyType  {

    private String id;
    private String charoff;
    private String title;
    private String dir;
    private String lang;
    private String lang1;
    private String class_;
    private String char;
    private String valign;
    private String align;
    private String style;





    private xhtml_TableType xhtml_tabletype;




    private List<xhtml_TrType> xhtml_trtypes;




    private xhtml_DocumentRoot xhtml_documentroot;


    public xhtml_TbodyType(
        String id,        String charoff,        String title,        String dir,        String lang,        String lang1,        String class_,        String char,        String valign,        String align,        String style    ) {
        this.id = id;
        this.charoff = charoff;
        this.title = title;
        this.dir = dir;
        this.lang = lang;
        this.lang1 = lang1;
        this.class_ = class_;
        this.char = char;
        this.valign = valign;
        this.align = align;
        this.style = style;
        this.xhtml_trtypes = new ArrayList<>();
    }

    public xhtml_TbodyType(
        String id,        String charoff,        String title,        String dir,        String lang,        String lang1,        String class_,        String char,        String valign,        String align,        String style        ArrayList<xhtml_TrType> xhtml_trtypes    ) {
        this.id = id;
        this.charoff = charoff;
        this.title = title;
        this.dir = dir;
        this.lang = lang;
        this.lang1 = lang1;
        this.class_ = class_;
        this.char = char;
        this.valign = valign;
        this.align = align;
        this.style = style;
        this.xhtml_trtypes = xhtml_trtypes;
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
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }
    public List<xhtml_TrType> getXhtml_trtypes() {
        return xhtml_trtypes;
    }

    public void addXhtml_trtype(Xhtml_trtype xhtml_trtype) {
        this.xhtml_trtypes.add(xhtml_trtype);
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }

}