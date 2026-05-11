





import java.util.List;
import java.util.ArrayList;

public class html_APPLET  {

    private String width;
    private String class_;
    private String align;
    private String src;
    private String applet;
    private String height;



    public html_APPLET(
        String width,        String class_,        String align,        String src,        String applet,        String height    ) {
        this.width = width;
        this.class_ = class_;
        this.align = align;
        this.src = src;
        this.applet = applet;
        this.height = height;
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