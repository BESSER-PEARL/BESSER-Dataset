





import java.util.List;
import java.util.ArrayList;

public class HTML_APPLET  {

    private String src;
    private String width;
    private String align;
    private String applet;
    private String height;
    private String class_;



    public HTML_APPLET(
        String src,        String width,        String align,        String applet,        String height,        String class_    ) {
        this.src = src;
        this.width = width;
        this.align = align;
        this.applet = applet;
        this.height = height;
        this.class_ = class_;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getApplet() {
        return applet;
    }

    public void setApplet(String applet) {
        this.applet = applet;
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


}