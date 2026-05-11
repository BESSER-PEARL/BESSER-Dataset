





import java.util.List;
import java.util.ArrayList;

public class xhtml_KbdType extends Inline {

    private String id;
    private String style;
    private String title;
    private String lang1;
    private String class_;
    private String dir;
    private String lang;



    public xhtml_KbdType(
        String id,        String style,        String title,        String lang1,        String class_,        String dir,        String lang    ) {
        super(
        );
        this.id = id;
        this.style = style;
        this.title = title;
        this.lang1 = lang1;
        this.class_ = class_;
        this.dir = dir;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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