





import java.util.List;
import java.util.ArrayList;

public class xhtml_Colgroup  {

    private String charoff;
    private String class_;
    private String lang;
    private String width;
    private String char;
    private String valign;
    private String span;
    private String style;
    private String align;





    private xhtml_Table xhtml_table;




    private List<xhtml_Col> xhtml_cols;


    public xhtml_Colgroup(
        String charoff,        String class_,        String lang,        String width,        String char,        String valign,        String span,        String style,        String align    ) {
        this.charoff = charoff;
        this.class_ = class_;
        this.lang = lang;
        this.width = width;
        this.char = char;
        this.valign = valign;
        this.span = span;
        this.style = style;
        this.align = align;
        this.xhtml_cols = new ArrayList<>();
    }

    public xhtml_Colgroup(
        String charoff,        String class_,        String lang,        String width,        String char,        String valign,        String span,        String style,        String align        ArrayList<xhtml_Col> xhtml_cols    ) {
        this.charoff = charoff;
        this.class_ = class_;
        this.lang = lang;
        this.width = width;
        this.char = char;
        this.valign = valign;
        this.span = span;
        this.style = style;
        this.align = align;
        this.xhtml_cols = xhtml_cols;
    }

    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
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

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }
    public List<xhtml_Col> getXhtml_cols() {
        return xhtml_cols;
    }

    public void addXhtml_col(Xhtml_col xhtml_col) {
        this.xhtml_cols.add(xhtml_col);
    }

}