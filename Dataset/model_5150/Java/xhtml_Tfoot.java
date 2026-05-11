





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tfoot  {

    private String charoff;
    private String valign;
    private String lang;
    private String char;
    private String style;
    private String align;
    private String class_;





    private xhtml_Table xhtml_table;


    public xhtml_Tfoot(
        String charoff,        String valign,        String lang,        String char,        String style,        String align,        String class_    ) {
        this.charoff = charoff;
        this.valign = valign;
        this.lang = lang;
        this.char = char;
        this.style = style;
        this.align = align;
        this.class_ = class_;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}