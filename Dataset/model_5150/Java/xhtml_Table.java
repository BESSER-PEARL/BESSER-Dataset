





import java.util.List;
import java.util.ArrayList;

public class xhtml_Table  {

    private String border;
    private String cellpadding;
    private String class_;
    private String hl7Id;
    private String cellspacing;
    private String lang;
    private String style;
    private String frame;
    private String width;
    private String rules;





    private xhtml_Caption xhtml_caption;




    private xhtml_Block xhtml_block;




    private xhtml_Object xhtml_object;


    public xhtml_Table(
        String border,        String cellpadding,        String class_,        String hl7Id,        String cellspacing,        String lang,        String style,        String frame,        String width,        String rules    ) {
        this.border = border;
        this.cellpadding = cellpadding;
        this.class_ = class_;
        this.hl7Id = hl7Id;
        this.cellspacing = cellspacing;
        this.lang = lang;
        this.style = style;
        this.frame = frame;
        this.width = width;
        this.rules = rules;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getHl7id() {
        return hl7Id;
    }

    public void setHl7id(String hl7Id) {
        this.hl7Id = hl7Id;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
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
    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }

    public xhtml_Caption getXhtml_caption() {
        return xhtml_caption;
    }

    public void setXhtml_caption(xhtml_Caption xhtml_caption) {
        this.xhtml_caption = xhtml_caption;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }

}