





import java.util.List;
import java.util.ArrayList;

public class xhtml_TrType  {

    private String group;
    private String id;
    private String style;
    private String valign;
    private String char;
    private String class_;
    private String align;
    private String charoff;
    private String title;





    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_TdType> xhtml_tdtypes;




    private xhtml_TheadType xhtml_theadtype;




    private List<xhtml_ThType> xhtml_thtypes;




    private xhtml_TfootType xhtml_tfoottype;




    private xhtml_TbodyType xhtml_tbodytype;




    private xhtml_TableType xhtml_tabletype;


    public xhtml_TrType(
        String group,        String id,        String style,        String valign,        String char,        String class_,        String align,        String charoff,        String title    ) {
        this.group = group;
        this.id = id;
        this.style = style;
        this.valign = valign;
        this.char = char;
        this.class_ = class_;
        this.align = align;
        this.charoff = charoff;
        this.title = title;
        this.xhtml_tdtypes = new ArrayList<>();
        this.xhtml_thtypes = new ArrayList<>();
    }

    public xhtml_TrType(
        String group,        String id,        String style,        String valign,        String char,        String class_,        String align,        String charoff,        String title        ArrayList<xhtml_TdType> xhtml_tdtypes,        ArrayList<xhtml_ThType> xhtml_thtypes    ) {
        this.group = group;
        this.id = id;
        this.style = style;
        this.valign = valign;
        this.char = char;
        this.class_ = class_;
        this.align = align;
        this.charoff = charoff;
        this.title = title;
        this.xhtml_tdtypes = xhtml_tdtypes;
        this.xhtml_thtypes = xhtml_thtypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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
    public xhtml_TheadType getXhtml_theadtype() {
        return xhtml_theadtype;
    }

    public void setXhtml_theadtype(xhtml_TheadType xhtml_theadtype) {
        this.xhtml_theadtype = xhtml_theadtype;
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
    public xhtml_TbodyType getXhtml_tbodytype() {
        return xhtml_tbodytype;
    }

    public void setXhtml_tbodytype(xhtml_TbodyType xhtml_tbodytype) {
        this.xhtml_tbodytype = xhtml_tbodytype;
    }
    public xhtml_TableType getXhtml_tabletype() {
        return xhtml_tabletype;
    }

    public void setXhtml_tabletype(xhtml_TableType xhtml_tabletype) {
        this.xhtml_tabletype = xhtml_tabletype;
    }

}