





import java.util.List;
import java.util.ArrayList;

public class xhtml_ImgType  {

    private String width;
    private String title;
    private String src;
    private String dir;
    private String style;
    private String usemap;
    private String id;
    private String height;
    private String class_;
    private String ismap;
    private String lang1;
    private String alt;
    private String longdesc;
    private String lang;





    private xhtml_AContent xhtml_acontent;


    public xhtml_ImgType(
        String width,        String title,        String src,        String dir,        String style,        String usemap,        String id,        String height,        String class_,        String ismap,        String lang1,        String alt,        String longdesc,        String lang    ) {
        this.width = width;
        this.title = title;
        this.src = src;
        this.dir = dir;
        this.style = style;
        this.usemap = usemap;
        this.id = id;
        this.height = height;
        this.class_ = class_;
        this.ismap = ismap;
        this.lang1 = lang1;
        this.alt = alt;
        this.longdesc = longdesc;
        this.lang = lang;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
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
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }

    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }

}