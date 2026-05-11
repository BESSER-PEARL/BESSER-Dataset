





import java.util.List;
import java.util.ArrayList;

public class xhtml_Div extends Flow {

    private String style;
    private String hl7Id;
    private String lang;
    private String class_;
    private String title;





    private xhtml_Object xhtml_object;


    public xhtml_Div(
        String style,        String hl7Id,        String lang,        String class_,        String title    ) {
        super(
        );
        this.style = style;
        this.hl7Id = hl7Id;
        this.lang = lang;
        this.class_ = class_;
        this.title = title;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getHl7id() {
        return hl7Id;
    }

    public void setHl7id(String hl7Id) {
        this.hl7Id = hl7Id;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public xhtml_Object getXhtml_object() {
        return xhtml_object;
    }

    public void setXhtml_object(xhtml_Object xhtml_object) {
        this.xhtml_object = xhtml_object;
    }

}