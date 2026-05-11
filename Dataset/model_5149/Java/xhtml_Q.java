





import java.util.List;
import java.util.ArrayList;

public class xhtml_Q extends Inline {

    private String style;
    private String cite1;
    private String lang;
    private String class_;



    public xhtml_Q(
        String style,        String cite1,        String lang,        String class_    ) {
        super(
        );
        this.style = style;
        this.cite1 = cite1;
        this.lang = lang;
        this.class_ = class_;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getCite1() {
        return cite1;
    }

    public void setCite1(String cite1) {
        this.cite1 = cite1;
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


}