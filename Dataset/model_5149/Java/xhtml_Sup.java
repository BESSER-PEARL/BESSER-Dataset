





import java.util.List;
import java.util.ArrayList;

public class xhtml_Sup extends Inline {

    private String lang;
    private String style;
    private String class_;



    public xhtml_Sup(
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


}