





import java.util.List;
import java.util.ArrayList;

public class xhtml_BType extends Inline {

    private String lang1;
    private String dir;
    private String title;
    private String id;
    private String style;
    private String lang;
    private String class_;



    public xhtml_BType(
        String lang1,        String dir,        String title,        String id,        String style,        String lang,        String class_    ) {
        super(
        );
        this.lang1 = lang1;
        this.dir = dir;
        this.title = title;
        this.id = id;
        this.style = style;
        this.lang = lang;
        this.class_ = class_;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}