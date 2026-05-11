





import java.util.List;
import java.util.ArrayList;

public class xhtml_TrType  {

    private String id;
    private String charoff;
    private String group;
    private String style;
    private String align;
    private String char;
    private String title;
    private String valign;
    private String class_;





    private List<xhtml_ThType> xhtml_thtypes;




    private xhtml_TfootType xhtml_tfoottype;




    private List<xhtml_TdType> xhtml_tdtypes;




    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_TbodyType xhtml_tbodytype;




    private xhtml_TheadType xhtml_theadtype;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TrType(
        String id,        String charoff,        String group,        String style,        String align,        String char,        String title,        String valign,        String class_    ) {
        this.id = id;
        this.charoff = charoff;
        this.group = group;
        this.style = style;
        this.align = align;
        this.char = char;
        this.title = title;
        this.valign = valign;
        this.class_ = class_;
        this.xhtml_thtypes = new ArrayList<>();
        this.xhtml_tdtypes = new ArrayList<>();
    }

    public xhtml_TrType(
        String id,        String charoff,        String group,        String style,        String align,        String char,        String title,        String valign,        String class_        ArrayList<xhtml_ThType> xhtml_thtypes,        ArrayList<xhtml_TdType> xhtml_tdtypes    ) {
        this.id = id;
        this.charoff = charoff;
        this.group = group;
        this.style = style;
        this.align = align;
        this.char = char;
        this.title = title;
        this.valign = valign;
        this.class_ = class_;
        this.xhtml_thtypes = xhtml_thtypes;
        this.xhtml_tdtypes = xhtml_tdtypes;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public List<xhtml_ThType> getXhtml_thtypes() {
        return xhtml_thtypes;
    }

    public void addXhtml_thtype(Xhtml_thtype xhtml_thtype) {
        this.xhtml_thtypes.add(xhtml_thtype);
    }
    public xhtml_TfootType getXhtml_tfoottype() {
        return xhtml_tfoottype;
    }

    public void setXhtml_tfoottype(xhtml_TfootType xhtml_tfoottype) {
        this.xhtml_tfoottype = xhtml_tfoottype;
    }
    public List<xhtml_TdType> getXhtml_tdtypes() {
        return xhtml_tdtypes;
    }

    public void addXhtml_tdtype(Xhtml_tdtype xhtml_tdtype) {
        this.xhtml_tdtypes.add(xhtml_tdtype);
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_TbodyType getXhtml_tbodytype() {
        return xhtml_tbodytype;
    }

    public void setXhtml_tbodytype(xhtml_TbodyType xhtml_tbodytype) {
        this.xhtml_tbodytype = xhtml_tbodytype;
    }
    public xhtml_TheadType getXhtml_theadtype() {
        return xhtml_theadtype;
    }

    public void setXhtml_theadtype(xhtml_TheadType xhtml_theadtype) {
        this.xhtml_theadtype = xhtml_theadtype;
    }
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}