





import java.util.List;
import java.util.ArrayList;

public class xhtml_Dd extends Flow {

    private String style;
    private String class_;
    private String lang;





    private xhtml_Dl xhtml_dl;


    public xhtml_Dd(
        String style,        String class_,        String lang    ) {
        super(
        );
        this.style = style;
        this.class_ = class_;
        this.lang = lang;
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

    public xhtml_Dl getXhtml_dl() {
        return xhtml_dl;
    }

    public void setXhtml_dl(xhtml_Dl xhtml_dl) {
        this.xhtml_dl = xhtml_dl;
    }

}