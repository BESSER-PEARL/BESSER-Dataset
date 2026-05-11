





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tbody  {

    private String class_;
    private String char;
    private String align;
    private String valign;
    private String lang;
    private String style;
    private String charoff;





    private xhtml_Table xhtml_table;


    public xhtml_Tbody(
        String class_,        String char,        String align,        String valign,        String lang,        String style,        String charoff    ) {
        this.class_ = class_;
        this.char = char;
        this.align = align;
        this.valign = valign;
        this.lang = lang;
        this.style = style;
        this.charoff = charoff;
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