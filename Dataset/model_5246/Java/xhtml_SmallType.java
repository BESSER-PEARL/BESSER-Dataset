





import java.util.List;
import java.util.ArrayList;

public class xhtml_SmallType extends Inline {

    private String lang;
    private String lang1;
    private String title;
    private String dir;
    private String id;
    private String style;
    private String class_;



    public xhtml_SmallType(
        String lang,        String lang1,        String title,        String dir,        String id,        String style,        String class_    ) {
        super(
        );
        this.lang = lang;
        this.lang1 = lang1;
        this.title = title;
        this.dir = dir;
        this.id = id;
        this.style = style;
        this.class_ = class_;
    }


    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}