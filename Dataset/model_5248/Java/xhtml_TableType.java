





import java.util.List;
import java.util.ArrayList;

public class xhtml_TableType  {

    private String cellspacing;
    private String border;
    private String width;
    private String id;
    private String title;
    private String class_;
    private String summary;
    private String cellpadding;
    private String style;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_CaptionType xhtml_captiontype;


    public xhtml_TableType(
        String cellspacing,        String border,        String width,        String id,        String title,        String class_,        String summary,        String cellpadding,        String style    ) {
        this.cellspacing = cellspacing;
        this.border = border;
        this.width = width;
        this.id = id;
        this.title = title;
        this.class_ = class_;
        this.summary = summary;
        this.cellpadding = cellpadding;
        this.style = style;
    }


    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_CaptionType getXhtml_captiontype() {
        return xhtml_captiontype;
    }

    public void setXhtml_captiontype(xhtml_CaptionType xhtml_captiontype) {
        this.xhtml_captiontype = xhtml_captiontype;
    }

}