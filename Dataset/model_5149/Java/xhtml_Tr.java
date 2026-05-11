





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tr  {

    private String char;
    private String group;
    private String lang;
    private String valign;
    private String class_;
    private String style;
    private String align;
    private String charoff;





    private xhtml_Table xhtml_table;




    private List<xhtml_Th> xhtml_ths;




    private xhtml_Thead xhtml_thead;




    private List<xhtml_Td> xhtml_tds;




    private xhtml_Tbody xhtml_tbody;




    private xhtml_Tfoot xhtml_tfoot;


    public xhtml_Tr(
        String char,        String group,        String lang,        String valign,        String class_,        String style,        String align,        String charoff    ) {
        this.char = char;
        this.group = group;
        this.lang = lang;
        this.valign = valign;
        this.class_ = class_;
        this.style = style;
        this.align = align;
        this.charoff = charoff;
        this.xhtml_ths = new ArrayList<>();
        this.xhtml_tds = new ArrayList<>();
    }

    public xhtml_Tr(
        String char,        String group,        String lang,        String valign,        String class_,        String style,        String align,        String charoff        ArrayList<xhtml_Th> xhtml_ths,        ArrayList<xhtml_Td> xhtml_tds    ) {
        this.char = char;
        this.group = group;
        this.lang = lang;
        this.valign = valign;
        this.class_ = class_;
        this.style = style;
        this.align = align;
        this.charoff = charoff;
        this.xhtml_ths = xhtml_ths;
        this.xhtml_tds = xhtml_tds;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
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
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }
    public List<xhtml_Th> getXhtml_ths() {
        return xhtml_ths;
    }

    public void addXhtml_th(Xhtml_th xhtml_th) {
        this.xhtml_ths.add(xhtml_th);
    }
    public xhtml_Thead getXhtml_thead() {
        return xhtml_thead;
    }

    public void setXhtml_thead(xhtml_Thead xhtml_thead) {
        this.xhtml_thead = xhtml_thead;
    }
    public List<xhtml_Td> getXhtml_tds() {
        return xhtml_tds;
    }

    public void addXhtml_td(Xhtml_td xhtml_td) {
        this.xhtml_tds.add(xhtml_td);
    }
    public xhtml_Tbody getXhtml_tbody() {
        return xhtml_tbody;
    }

    public void setXhtml_tbody(xhtml_Tbody xhtml_tbody) {
        this.xhtml_tbody = xhtml_tbody;
    }
    public xhtml_Tfoot getXhtml_tfoot() {
        return xhtml_tfoot;
    }

    public void setXhtml_tfoot(xhtml_Tfoot xhtml_tfoot) {
        this.xhtml_tfoot = xhtml_tfoot;
    }

}