





import java.util.List;
import java.util.ArrayList;

public class xhtml_BdoType extends Inline {

    private String dir;
    private String lang1;
    private String title;
    private String lang;
    private String id;
    private String style;
    private String class_;



    public xhtml_BdoType(
        String dir,        String lang1,        String title,        String lang,        String id,        String style,        String class_    ) {
        super(
        );
        this.dir = dir;
        this.lang1 = lang1;
        this.title = title;
        this.lang = lang;
        this.id = id;
        this.style = style;
        this.class_ = class_;
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