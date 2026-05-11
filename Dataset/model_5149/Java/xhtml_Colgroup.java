





import java.util.List;
import java.util.ArrayList;

public class xhtml_Colgroup  {

    private String style;
    private String span;
    private String charoff;
    private String char;
    private String class_;
    private String align;
    private String valign;
    private String width;
    private String lang;





    private List<xhtml_Col> xhtml_cols;




    private xhtml_Table xhtml_table;


    public xhtml_Colgroup(
        String style,        String span,        String charoff,        String char,        String class_,        String align,        String valign,        String width,        String lang    ) {
        this.style = style;
        this.span = span;
        this.charoff = charoff;
        this.char = char;
        this.class_ = class_;
        this.align = align;
        this.valign = valign;
        this.width = width;
        this.lang = lang;
        this.xhtml_cols = new ArrayList<>();
    }

    public xhtml_Colgroup(
        String style,        String span,        String charoff,        String char,        String class_,        String align,        String valign,        String width,        String lang        ArrayList<xhtml_Col> xhtml_cols    ) {
        this.style = style;
        this.span = span;
        this.charoff = charoff;
        this.char = char;
        this.class_ = class_;
        this.align = align;
        this.valign = valign;
        this.width = width;
        this.lang = lang;
        this.xhtml_cols = xhtml_cols;
    }

    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
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
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }

    public List<xhtml_Col> getXhtml_cols() {
        return xhtml_cols;
    }

    public void addXhtml_col(Xhtml_col xhtml_col) {
        this.xhtml_cols.add(xhtml_col);
    }
    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}