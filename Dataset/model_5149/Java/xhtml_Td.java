





import java.util.List;
import java.util.ArrayList;

public class xhtml_Td extends Flow {

    private String lang;
    private String char;
    private String rowspan;
    private String style;
    private String charoff;
    private String align;
    private String class_;
    private String colspan;
    private String valign;



    public xhtml_Td(
        String lang,        String char,        String rowspan,        String style,        String charoff,        String align,        String class_,        String colspan,        String valign    ) {
        super(
        );
        this.lang = lang;
        this.char = char;
        this.rowspan = rowspan;
        this.style = style;
        this.charoff = charoff;
        this.align = align;
        this.class_ = class_;
        this.colspan = colspan;
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
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
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
    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }


}