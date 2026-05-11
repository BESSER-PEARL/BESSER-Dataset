





import java.util.List;
import java.util.ArrayList;

public class xhtml_Th extends Flow {

    private String valign;
    private String rowspan;
    private String class_;
    private String lang;
    private String charoff;
    private String align;
    private String char;
    private String style;
    private String colspan;



    public xhtml_Th(
        String valign,        String rowspan,        String class_,        String lang,        String charoff,        String align,        String char,        String style,        String colspan    ) {
        super(
        );
        this.valign = valign;
        this.rowspan = rowspan;
        this.class_ = class_;
        this.lang = lang;
        this.charoff = charoff;
        this.align = align;
        this.char = char;
        this.style = style;
        this.colspan = colspan;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
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
    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
    }


}