





import java.util.List;
import java.util.ArrayList;

public class html_APPLET  {

    private String applet;
    private String width;
    private String src;
    private String class_;
    private String align;
    private String height;



    public html_APPLET(
        String applet,        String width,        String src,        String class_,        String align,        String height    ) {
        this.applet = applet;
        this.width = width;
        this.src = src;
        this.class_ = class_;
        this.align = align;
        this.height = height;
    }


    public String getApplet() {
        return applet;
    }

    public void setApplet(String applet) {
        this.applet = applet;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}