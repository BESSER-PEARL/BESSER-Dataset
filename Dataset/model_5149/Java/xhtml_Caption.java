





import java.util.List;
import java.util.ArrayList;

public class xhtml_Caption extends Inline {

    private String class_;
    private String style;
    private String lang;



    public xhtml_Caption(
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


}