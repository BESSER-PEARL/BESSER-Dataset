





import java.util.List;
import java.util.ArrayList;

public class xhtml_Q extends Inline {

    private String cite1;
    private String style;
    private String class_;
    private String lang;



    public xhtml_Q(
        String cite1,        String style,        String class_,        String lang    ) {
        super(
        );
        this.cite1 = cite1;
        this.style = style;
        this.class_ = class_;
        this.lang = lang;
    }


    public String getCite1() {
        return cite1;
    }

    public void setCite1(String cite1) {
        this.cite1 = cite1;
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