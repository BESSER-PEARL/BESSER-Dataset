





import java.util.List;
import java.util.ArrayList;

public class xhtml_Img  {

    private String imageType;
    private String width;
    private String class_;
    private String height;
    private String hl7Id;
    private String lang;
    private String src;
    private String style;
    private String alt;





    private xhtml_Object xhtml_object;




    private xhtml_Img xhtml_img;


    public xhtml_Img(
        String imageType,        String width,        String class_,        String height,        String hl7Id,        String lang,        String src,        String style,        String alt    ) {
        this.imageType = imageType;
        this.width = width;
        this.class_ = class_;
        this.height = height;
        this.hl7Id = hl7Id;
        this.lang = lang;
        this.src = src;
        this.style = style;
        this.alt = alt;
    }


    public String getImagetype() {
        return imageType;
    }

    public void setImagetype(String imageType) {
        this.imageType = imageType;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
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