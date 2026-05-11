





import java.util.List;
import java.util.ArrayList;

public class xhtml_TrType  {

    private String char;
    private String charoff;
    private String style;
    private String align;
    private String group;
    private String title;
    private String valign;
    private String id;
    private String class_;





    private xhtml_TableType xhtml_tabletype;




    private List<xhtml_ThType> xhtml_thtypes;




    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_TdType> xhtml_tdtypes;


    public xhtml_TrType(
        String char,        String charoff,        String style,        String align,        String group,        String title,        String valign,        String id,        String class_    ) {
        this.char = char;
        this.charoff = charoff;
        this.style = style;
        this.align = align;
        this.group = group;
        this.title = title;
        this.valign = valign;
        this.id = id;
        this.class_ = class_;
        this.xhtml_thtypes = new ArrayList<>();
        this.xhtml_tdtypes = new ArrayList<>();
    }

    public xhtml_TrType(
        String char,        String charoff,        String style,        String align,        String group,        String title,        String valign,        String id,        String class_        ArrayList<xhtml_ThType> xhtml_thtypes,        ArrayList<xhtml_TdType> xhtml_tdtypes    ) {
        this.char = char;
        this.charoff = charoff;
        this.style = style;
        this.align = align;
        this.group = group;
        this.title = title;
        this.valign = valign;
        this.id = id;
        this.class_ = class_;
        this.xhtml_thtypes = xhtml_thtypes;
        this.xhtml_tdtypes = xhtml_tdtypes;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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

    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }
    public List<xhtml_ThType> getXhtml_thtypes() {
        return xhtml_thtypes;
    }

    public void addXhtml_thtype(Xhtml_thtype xhtml_thtype) {
        this.xhtml_thtypes.add(xhtml_thtype);
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public List<xhtml_TdType> getXhtml_tdtypes() {
        return xhtml_tdtypes;
    }

    public void addXhtml_tdtype(Xhtml_tdtype xhtml_tdtype) {
        this.xhtml_tdtypes.add(xhtml_tdtype);
    }

}