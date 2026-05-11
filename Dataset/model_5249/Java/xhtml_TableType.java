





import java.util.List;
import java.util.ArrayList;

public class xhtml_TableType  {

    private String title;
    private String border;
    private String style;
    private String width;
    private String summary;
    private String id;
    private String class_;
    private String cellspacing;
    private String cellpadding;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_Block xhtml_block;




    private xhtml_CaptionType xhtml_captiontype;


    public xhtml_TableType(
        String title,        String border,        String style,        String width,        String summary,        String id,        String class_,        String cellspacing,        String cellpadding    ) {
        this.title = title;
        this.border = border;
        this.style = style;
        this.width = width;
        this.summary = summary;
        this.id = id;
        this.class_ = class_;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
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

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_CaptionType getXhtml_captiontype() {
        return xhtml_captiontype;
    }

    public void setXhtml_captiontype(xhtml_CaptionType xhtml_captiontype) {
        this.xhtml_captiontype = xhtml_captiontype;
    }

}