





import java.util.List;
import java.util.ArrayList;

public class xhtml_Table  {

    private String hl7Id;
    private String rules;
    private String frame;
    private String style;
    private String cellspacing;
    private String cellpadding;
    private String class_;
    private String border;
    private String width;
    private String lang;





    private xhtml_Caption xhtml_caption;




    private xhtml_Object xhtml_object;




    private xhtml_Block xhtml_block;


    public xhtml_Table(
        String hl7Id,        String rules,        String frame,        String style,        String cellspacing,        String cellpadding,        String class_,        String border,        String width,        String lang    ) {
        this.hl7Id = hl7Id;
        this.rules = rules;
        this.frame = frame;
        this.style = style;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
        this.class_ = class_;
        this.border = border;
        this.width = width;
        this.lang = lang;
    }


    public String getHl7id() {
        return hl7Id;
    }

    public void setHl7id(String hl7Id) {
        this.hl7Id = hl7Id;
    }
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }
    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }

    public xhtml_Caption getXhtml_caption() {
        return xhtml_caption;
    }

    public void setXhtml_caption(xhtml_Caption xhtml_caption) {
        this.xhtml_caption = xhtml_caption;
    }
    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}