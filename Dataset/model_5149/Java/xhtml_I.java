





import java.util.List;
import java.util.ArrayList;

public class xhtml_I extends Inline {

    private String style;
    private String class_;
    private String lang;



    public xhtml_I(
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


}