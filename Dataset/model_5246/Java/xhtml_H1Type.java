





import java.util.List;
import java.util.ArrayList;

public class xhtml_H1Type extends Inline {

    private String lang;
    private String dir;
    private String title;
    private String lang1;
    private String style;
    private String id;
    private String class_;



    public xhtml_H1Type(
        String lang,        String dir,        String title,        String lang1,        String style,        String id,        String class_    ) {
        super(
        );
        this.lang = lang;
        this.dir = dir;
        this.title = title;
        this.lang1 = lang1;
        this.style = style;
        this.id = id;
        this.class_ = class_;
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


}