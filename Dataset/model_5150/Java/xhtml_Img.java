





import java.util.List;
import java.util.ArrayList;

public class xhtml_Img  {

    private String width;
    private String alt;
    private String height;
    private String hl7Id;
    private String src;
    private String imageType;
    private String style;
    private String class_;
    private String lang;





    private xhtml_Object xhtml_object;




    private xhtml_Img xhtml_img;


    public xhtml_Img(
        String width,        String alt,        String height,        String hl7Id,        String src,        String imageType,        String style,        String class_,        String lang    ) {
        this.width = width;
        this.alt = alt;
        this.height = height;
        this.hl7Id = hl7Id;
        this.src = src;
        this.imageType = imageType;
        this.style = style;
        this.class_ = class_;
        this.lang = lang;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getHl7id() {
        return hl7Id;
    }

    public void setHl7id(String hl7Id) {
        this.hl7Id = hl7Id;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getImagetype() {
        return imageType;
    }

    public void setImagetype(String imageType) {
        this.imageType = imageType;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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

    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }
    public xhtml_Img getXhtml_img() {
        return xhtml_img;
    }

    public void setXhtml_img(xhtml_Img xhtml_img) {
        this.xhtml_img = xhtml_img;
    }

}