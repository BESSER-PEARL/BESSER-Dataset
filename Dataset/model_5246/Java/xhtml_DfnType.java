





import java.util.List;
import java.util.ArrayList;

public class xhtml_DfnType extends Inline {

    private String class_;
    private String style;
    private String title;
    private String lang1;
    private String id;
    private String dir;
    private String lang;



    public xhtml_DfnType(
        String class_,        String style,        String title,        String lang1,        String id,        String dir,        String lang    ) {
        super(
        );
        this.class_ = class_;
        this.style = style;
        this.title = title;
        this.lang1 = lang1;
        this.id = id;
        this.dir = dir;
        this.lang = lang;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }


}