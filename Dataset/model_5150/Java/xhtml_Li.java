





import java.util.List;
import java.util.ArrayList;

public class xhtml_Li extends Flow {

    private String class_;
    private String style;
    private String lang;





    private xhtml_Ul xhtml_ul;




    private xhtml_Ol xhtml_ol;


    public xhtml_Li(
        String class_,        String style,        String lang    ) {
        super(
        );
        this.class_ = class_;
        this.style = style;
        this.lang = lang;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }

    public xhtml_Ul getXhtml_ul() {
        return xhtml_ul;
    }

    public void setXhtml_ul(xhtml_Ul xhtml_ul) {
        this.xhtml_ul = xhtml_ul;
    }
    public xhtml_Ol getXhtml_ol() {
        return xhtml_ol;
    }

    public void setXhtml_ol(xhtml_Ol xhtml_ol) {
        this.xhtml_ol = xhtml_ol;
    }

}