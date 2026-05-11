





import java.util.List;
import java.util.ArrayList;

public class xhtml_Tt extends Inline {

    private String class_;
    private String lang;
    private String style;



    public xhtml_Tt(
        String class_,        String lang,        String style    ) {
        super(
        );
        this.class_ = class_;
        this.lang = lang;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}