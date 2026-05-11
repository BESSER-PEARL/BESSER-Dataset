





import java.util.List;
import java.util.ArrayList;

public class xhtml_Li extends Flow {

    private String lang;
    private String style;
    private String class_;





    private xhtml_Ol xhtml_ol;




    private xhtml_Ul xhtml_ul;


    public xhtml_Li(
        String lang,        String style,        String class_    ) {
        super(
        );
        this.lang = lang;
        this.style = style;
        this.class_ = class_;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
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

    public xhtml_Ol getXhtml_ol() {
        return xhtml_ol;
    }

    public void setXhtml_ol(xhtml_Ol xhtml_ol) {
        this.xhtml_ol = xhtml_ol;
    }
    public xhtml_Ul getXhtml_ul() {
        return xhtml_ul;
    }

    public void setXhtml_ul(xhtml_Ul xhtml_ul) {
        this.xhtml_ul = xhtml_ul;
    }

}