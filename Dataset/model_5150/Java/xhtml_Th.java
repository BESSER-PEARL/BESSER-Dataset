





import java.util.List;
import java.util.ArrayList;

public class xhtml_Th extends Flow {

    private String colspan;
    private String char;
    private String valign;
    private String class_;
    private String style;
    private String lang;
    private String rowspan;
    private String charoff;
    private String align;



    public xhtml_Th(
        String colspan,        String char,        String valign,        String class_,        String style,        String lang,        String rowspan,        String charoff,        String align    ) {
        super(
        );
        this.colspan = colspan;
        this.char = char;
        this.valign = valign;
        this.class_ = class_;
        this.style = style;
        this.lang = lang;
        this.rowspan = rowspan;
        this.charoff = charoff;
        this.align = align;
    }


    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}