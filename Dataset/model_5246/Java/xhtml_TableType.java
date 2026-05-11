





import java.util.List;
import java.util.ArrayList;

public class xhtml_TableType  {

    private String width;
    private String lang1;
    private String id;
    private String class_;
    private String title;
    private String rules;
    private String cellpadding;
    private String frame;
    private String summary;
    private String lang;
    private String style;
    private String border;
    private String dir;
    private String cellspacing;





    private xhtml_CaptionType xhtml_captiontype;




    private xhtml_Block xhtml_block;




    private xhtml_MapType xhtml_maptype;


    public xhtml_TableType(
        String width,        String lang1,        String id,        String class_,        String title,        String rules,        String cellpadding,        String frame,        String summary,        String lang,        String style,        String border,        String dir,        String cellspacing    ) {
        this.width = width;
        this.lang1 = lang1;
        this.id = id;
        this.class_ = class_;
        this.title = title;
        this.rules = rules;
        this.cellpadding = cellpadding;
        this.frame = frame;
        this.summary = summary;
        this.lang = lang;
        this.style = style;
        this.border = border;
        this.dir = dir;
        this.cellspacing = cellspacing;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
    }

    public xhtml_CaptionType getXhtml_captiontype() {
        return xhtml_captiontype;
    }

    public void setXhtml_captiontype(xhtml_CaptionType xhtml_captiontype) {
        this.xhtml_captiontype = xhtml_captiontype;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_MapType getXhtml_maptype() {
        return xhtml_maptype;
    }

    public void setXhtml_maptype(xhtml_MapType xhtml_maptype) {
        this.xhtml_maptype = xhtml_maptype;
    }

}