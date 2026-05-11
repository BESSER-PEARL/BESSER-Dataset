





import java.util.List;
import java.util.ArrayList;

public class xhtml_Thead  {

    private String class_;
    private String style;
    private String charoff;
    private String lang;
    private String align;
    private String valign;
    private String char;





    private xhtml_Table xhtml_table;


    public xhtml_Thead(
        String class_,        String style,        String charoff,        String lang,        String align,        String valign,        String char    ) {
        this.class_ = class_;
        this.style = style;
        this.charoff = charoff;
        this.lang = lang;
        this.align = align;
        this.valign = valign;
        this.char = char;
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
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }

    public xhtml_Table getXhtml_table() {
        return xhtml_table;
    }

    public void setXhtml_table(xhtml_Table xhtml_table) {
        this.xhtml_table = xhtml_table;
    }

}