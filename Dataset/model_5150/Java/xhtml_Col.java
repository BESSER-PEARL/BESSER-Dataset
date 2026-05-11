





import java.util.List;
import java.util.ArrayList;

public class xhtml_Col  {

    private String valign;
    private String charoff;
    private String char;
    private String lang;
    private String width;
    private String span;
    private String style;
    private String class_;
    private String align;





    private xhtml_Table xhtml_table;


    public xhtml_Col(
        String valign,        String charoff,        String char,        String lang,        String width,        String span,        String style,        String class_,        String align    ) {
        this.valign = valign;
        this.charoff = charoff;
        this.char = char;
        this.lang = lang;
        this.width = width;
        this.span = span;
        this.style = style;
        this.class_ = class_;
        this.align = align;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}