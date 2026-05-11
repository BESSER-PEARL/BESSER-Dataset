





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tbody  {

    private String align;
    private String style;
    private String class_;
    private String lang;
    private String char;
    private String valign;
    private String charoff;





    private xhtml_Table xhtml_table;


    public xhtml_Tbody(
        String align,        String style,        String class_,        String lang,        String char,        String valign,        String charoff    ) {
        this.align = align;
        this.style = style;
        this.class_ = class_;
        this.lang = lang;
        this.char = char;
        this.valign = valign;
        this.charoff = charoff;
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

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}