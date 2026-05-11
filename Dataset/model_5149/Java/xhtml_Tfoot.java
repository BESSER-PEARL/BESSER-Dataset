





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tfoot  {

    private String align;
    private String charoff;
    private String style;
    private String char;
    private String class_;
    private String valign;
    private String lang;





    private xhtml_Table xhtml_table;


    public xhtml_Tfoot(
        String align,        String charoff,        String style,        String char,        String class_,        String valign,        String lang    ) {
        this.align = align;
        this.charoff = charoff;
        this.style = style;
        this.char = char;
        this.class_ = class_;
        this.valign = valign;
        this.lang = lang;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}