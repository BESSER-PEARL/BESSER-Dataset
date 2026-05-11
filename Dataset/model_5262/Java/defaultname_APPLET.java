





import java.util.List;
import java.util.ArrayList;

public class defaultname_APPLET  {

    private String class_;
    private String align;
    private String width;
    private String height;
    private String applet;
    private String src;



    public defaultname_APPLET(
        String class_,        String align,        String width,        String height,        String applet,        String src    ) {
        this.class_ = class_;
        this.align = align;
        this.width = width;
        this.height = height;
        this.applet = applet;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getApplet() {
        return applet;
    }

    public void setApplet(String applet) {
        this.applet = applet;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}