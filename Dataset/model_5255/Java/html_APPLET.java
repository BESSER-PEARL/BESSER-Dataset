





import java.util.List;
import java.util.ArrayList;

public class html_APPLET  {

    private String src;
    private String align;
    private String class_;
    private String width;
    private String applet;
    private String height;



    public html_APPLET(
        String src,        String align,        String class_,        String width,        String applet,        String height    ) {
        this.src = src;
        this.align = align;
        this.class_ = class_;
        this.width = width;
        this.applet = applet;
        this.height = height;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}