





import java.util.List;
import java.util.ArrayList;

public class HTML_APPLET  {

    private String align;
    private String src;
    private String width;
    private String applet;
    private String class_;
    private String height;



    public HTML_APPLET(
        String align,        String src,        String width,        String applet,        String class_,        String height    ) {
        this.align = align;
        this.src = src;
        this.width = width;
        this.applet = applet;
        this.class_ = class_;
        this.height = height;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public String getApplet() {
        return applet;
    }

    public void setApplet(String applet) {
        this.applet = applet;
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


}