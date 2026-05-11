





import java.util.List;
import java.util.ArrayList;

public class xhtml_PType extends Inline {

    private String title;
    private String lang1;
    private String style;
    private String class_;
    private String id;
    private String lang;
    private String dir;



    public xhtml_PType(
        String title,        String lang1,        String style,        String class_,        String id,        String lang,        String dir    ) {
        super(
        );
        this.title = title;
        this.lang1 = lang1;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.lang = lang;
        this.dir = dir;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}