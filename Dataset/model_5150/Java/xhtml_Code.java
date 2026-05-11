





import java.util.List;
import java.util.ArrayList;

public class xhtml_Code extends Inline {

    private String lang;
    private String class_;
    private String style;



    public xhtml_Code(
        String lang,        String class_,        String style    ) {
        super(
        );
        this.lang = lang;
        this.class_ = class_;
        this.style = style;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
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


}