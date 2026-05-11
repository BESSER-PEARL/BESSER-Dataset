





import java.util.List;
import java.util.ArrayList;

public class xhtml_TrType  {

    private String lang1;
    private String align;
    private String style;
    private String char;
    private String group;
    private String charoff;
    private String valign;
    private String title;
    private String class_;
    private String lang;
    private String dir;
    private String id;





    private xhtml_TableType xhtml_tabletype;




    private xhtml_TfootType xhtml_tfoottype;




    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_TheadType xhtml_theadtype;




    private List<xhtml_TdType> xhtml_tdtypes;




    private List<xhtml_ThType> xhtml_thtypes;


    public xhtml_TrType(
        String lang1,        String align,        String style,        String char,        String group,        String charoff,        String valign,        String title,        String class_,        String lang,        String dir,        String id    ) {
        this.lang1 = lang1;
        this.align = align;
        this.style = style;
        this.char = char;
        this.group = group;
        this.charoff = charoff;
        this.valign = valign;
        this.title = title;
        this.class_ = class_;
        this.lang = lang;
        this.dir = dir;
        this.id = id;
        this.xhtml_tdtypes = new ArrayList<>();
        this.xhtml_thtypes = new ArrayList<>();
    }

    public xhtml_TrType(
        String lang1,        String align,        String style,        String char,        String group,        String charoff,        String valign,        String title,        String class_,        String lang,        String dir,        String id        ArrayList<xhtml_TdType> xhtml_tdtypes,        ArrayList<xhtml_ThType> xhtml_thtypes    ) {
        this.lang1 = lang1;
        this.align = align;
        this.style = style;
        this.char = char;
        this.group = group;
        this.charoff = charoff;
        this.valign = valign;
        this.title = title;
        this.class_ = class_;
        this.lang = lang;
        this.dir = dir;
        this.id = id;
        this.xhtml_tdtypes = xhtml_tdtypes;
        this.xhtml_thtypes = xhtml_thtypes;
    }

    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
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
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }
    public xhtml_TfootType getXhtml_tfoottype() {
        return xhtml_tfoottype;
    }

    public void setXhtml_tfoottype(xhtml_TfootType xhtml_tfoottype) {
        this.xhtml_tfoottype = xhtml_tfoottype;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_TheadType getXhtml_theadtype() {
        return xhtml_theadtype;
    }

    public void setXhtml_theadtype(xhtml_TheadType xhtml_theadtype) {
        this.xhtml_theadtype = xhtml_theadtype;
    }
    public List<xhtml_TdType> getXhtml_tdtypes() {
        return xhtml_tdtypes;
    }

    public void addXhtml_tdtype(Xhtml_tdtype xhtml_tdtype) {
        this.xhtml_tdtypes.add(xhtml_tdtype);
    }
    public List<xhtml_ThType> getXhtml_thtypes() {
        return xhtml_thtypes;
    }

    public void addXhtml_thtype(Xhtml_thtype xhtml_thtype) {
        this.xhtml_thtypes.add(xhtml_thtype);
    }

}