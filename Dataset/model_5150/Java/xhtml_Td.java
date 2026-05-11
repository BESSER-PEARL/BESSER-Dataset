





import java.util.List;
import java.util.ArrayList;

public class xhtml_Td extends Flow {

    private String colspan;
    private String valign;
    private String char;
    private String style;
    private String charoff;
    private String rowspan;
    private String lang;
    private String align;
    private String class_;



    public xhtml_Td(
        String colspan,        String valign,        String char,        String style,        String charoff,        String rowspan,        String lang,        String align,        String class_    ) {
        super(
        );
        this.colspan = colspan;
        this.valign = valign;
        this.char = char;
        this.style = style;
        this.charoff = charoff;
        this.rowspan = rowspan;
        this.lang = lang;
        this.align = align;
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
    public String getCharoff() {
        return charoff;
    }

    public void setCharoff(String charoff) {
        this.charoff = charoff;
    }
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}