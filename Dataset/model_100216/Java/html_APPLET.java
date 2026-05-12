





import java.util.List;
import java.util.ArrayList;

public class html_APPLET  {

    private String align;
    private String height;
    private String width;
    private String src;
    private String class_;
    private String applet;



    public html_APPLET(
        String align,        String height,        String width,        String src,        String class_,        String applet    ) {
        this.align = align;
        this.height = height;
        this.width = width;
        this.src = src;
        this.class_ = class_;
        this.applet = applet;
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
    public String getApplet() {
        return applet;
    }

    public void setApplet(String applet) {
        this.applet = applet;
    }


}