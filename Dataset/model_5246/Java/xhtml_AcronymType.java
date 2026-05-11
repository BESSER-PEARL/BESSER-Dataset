





import java.util.List;
import java.util.ArrayList;

public class xhtml_AcronymType extends Inline {

    private String style;
    private String lang1;
    private String dir;
    private String id;
    private String class_;
    private String lang;
    private String title;



    public xhtml_AcronymType(
        String style,        String lang1,        String dir,        String id,        String class_,        String lang,        String title    ) {
        super(
        );
        this.style = style;
        this.lang1 = lang1;
        this.dir = dir;
        this.id = id;
        this.class_ = class_;
        this.lang = lang;
        this.title = title;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}