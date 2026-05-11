





import java.util.List;
import java.util.ArrayList;

public class xhtml_Col  {

    private String char;
    private String charoff;
    private String lang;
    private String style;
    private String class_;
    private String span;
    private String width;
    private String valign;
    private String align;





    private xhtml_Table xhtml_table;


    public xhtml_Col(
        String char,        String charoff,        String lang,        String style,        String class_,        String span,        String width,        String valign,        String align    ) {
        this.char = char;
        this.charoff = charoff;
        this.lang = lang;
        this.style = style;
        this.class_ = class_;
        this.span = span;
        this.width = width;
        this.valign = valign;
        this.align = align;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
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
    public String getSpan() {
        return span;
    }

    public void setSpan(String span) {
        this.span = span;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}