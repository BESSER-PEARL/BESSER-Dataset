





import java.util.List;
import java.util.ArrayList;

public class xhtml_BigType extends Inline {

    private String dir;
    private String lang1;
    private String title;
    private String class_;
    private String style;
    private String lang;
    private String id;



    public xhtml_BigType(
        String dir,        String lang1,        String title,        String class_,        String style,        String lang,        String id    ) {
        super(
        );
        this.dir = dir;
        this.lang1 = lang1;
        this.title = title;
        this.class_ = class_;
        this.style = style;
        this.lang = lang;
        this.id = id;
    }


    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}