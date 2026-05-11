





import java.util.List;
import java.util.ArrayList;

public class xhtml_ImgType  {

    private String ismap;
    private String class_;
    private String alt;
    private String longdesc;
    private String width;
    private String src;
    private String height;
    private String usemap;
    private String title;
    private String id;
    private String style;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_AContent xhtml_acontent;


    public xhtml_ImgType(
        String ismap,        String class_,        String alt,        String longdesc,        String width,        String src,        String height,        String usemap,        String title,        String id,        String style    ) {
        this.ismap = ismap;
        this.class_ = class_;
        this.alt = alt;
        this.longdesc = longdesc;
        this.width = width;
        this.src = src;
        this.height = height;
        this.usemap = usemap;
        this.title = title;
        this.id = id;
        this.style = style;
    }


    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getLongdesc() {
        return longdesc;
    }

    public void setLongdesc(String longdesc) {
        this.longdesc = longdesc;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }

}