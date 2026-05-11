





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tr  {

    private String charoff;
    private String valign;
    private String group;
    private String lang;
    private String align;
    private String style;
    private String class_;
    private String char;





    private xhtml_Tfoot xhtml_tfoot;




    private List<xhtml_Td> xhtml_tds;




    private xhtml_Thead xhtml_thead;




    private List<xhtml_Th> xhtml_ths;




    private xhtml_Table xhtml_table;




    private xhtml_Tbody xhtml_tbody;


    public xhtml_Tr(
        String charoff,        String valign,        String group,        String lang,        String align,        String style,        String class_,        String char    ) {
        this.charoff = charoff;
        this.valign = valign;
        this.group = group;
        this.lang = lang;
        this.align = align;
        this.style = style;
        this.class_ = class_;
        this.char = char;
        this.xhtml_tds = new ArrayList<>();
        this.xhtml_ths = new ArrayList<>();
    }

    public xhtml_Tr(
        String charoff,        String valign,        String group,        String lang,        String align,        String style,        String class_,        String char        ArrayList<xhtml_Td> xhtml_tds,        ArrayList<xhtml_Th> xhtml_ths    ) {
        this.charoff = charoff;
        this.valign = valign;
        this.group = group;
        this.lang = lang;
        this.align = align;
        this.style = style;
        this.class_ = class_;
        this.char = char;
        this.xhtml_tds = xhtml_tds;
        this.xhtml_ths = xhtml_ths;
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
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }

    public xhtml_Tfoot getXhtml_tfoot() {
        return xhtml_tfoot;
    }

    public void setXhtml_tfoot(xhtml_Tfoot xhtml_tfoot) {
        this.xhtml_tfoot = xhtml_tfoot;
    }
    public List<xhtml_Td> getXhtml_tds() {
        return xhtml_tds;
    }

    public void addXhtml_td(Xhtml_td xhtml_td) {
        this.xhtml_tds.add(xhtml_td);
    }
    public xhtml_Thead getXhtml_thead() {
        return xhtml_thead;
    }

    public void setXhtml_thead(xhtml_Thead xhtml_thead) {
        this.xhtml_thead = xhtml_thead;
    }
    public List<xhtml_Th> getXhtml_ths() {
        return xhtml_ths;
    }

    public void addXhtml_th(Xhtml_th xhtml_th) {
        this.xhtml_ths.add(xhtml_th);
    }
    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }
    public xhtml_Tbody getXhtml_tbody() {
        return xhtml_tbody;
    }

    public void setXhtml_tbody(xhtml_Tbody xhtml_tbody) {
        this.xhtml_tbody = xhtml_tbody;
    }

}