





import java.util.List;
import java.util.ArrayList;

public class xhtml_ImgType  {

    private String width;
    private String usemap;
    private String height;
    private String class_;
    private String title;
    private String alt;
    private String style;
    private String src;
    private String ismap;
    private String longdesc;
    private String id;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_AContent xhtml_acontent;


    public xhtml_ImgType(
        String width,        String usemap,        String height,        String class_,        String title,        String alt,        String style,        String src,        String ismap,        String longdesc,        String id    ) {
        this.width = width;
        this.usemap = usemap;
        this.height = height;
        this.class_ = class_;
        this.title = title;
        this.alt = alt;
        this.style = style;
        this.src = src;
        this.ismap = ismap;
        this.longdesc = longdesc;
        this.id = id;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getLongdesc() {
        return longdesc;
    }

    public void setLongdesc(String longdesc) {
        this.longdesc = longdesc;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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