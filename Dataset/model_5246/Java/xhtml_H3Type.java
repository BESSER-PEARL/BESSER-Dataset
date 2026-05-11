





import java.util.List;
import java.util.ArrayList;

public class xhtml_H3Type extends Inline {

    private String id;
    private String lang;
    private String style;
    private String lang1;
    private String title;
    private String dir;
    private String class_;



    public xhtml_H3Type(
        String id,        String lang,        String style,        String lang1,        String title,        String dir,        String class_    ) {
        super(
        );
        this.id = id;
        this.lang = lang;
        this.style = style;
        this.lang1 = lang1;
        this.title = title;
        this.dir = dir;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}