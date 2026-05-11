





import java.util.List;
import java.util.ArrayList;

public class xhtml_QType extends Inline {

    private String dir;
    private String class_;
    private String lang1;
    private String cite1;
    private String lang;
    private String style;
    private String title;
    private String id;



    public xhtml_QType(
        String dir,        String class_,        String lang1,        String cite1,        String lang,        String style,        String title,        String id    ) {
        super(
        );
        this.dir = dir;
        this.class_ = class_;
        this.lang1 = lang1;
        this.cite1 = cite1;
        this.lang = lang;
        this.style = style;
        this.title = title;
        this.id = id;
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
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getCite1() {
        return cite1;
    }

    public void setCite1(String cite1) {
        this.cite1 = cite1;
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


}