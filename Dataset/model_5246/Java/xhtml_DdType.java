





import java.util.List;
import java.util.ArrayList;

public class xhtml_DdType extends Flow {

    private String lang1;
    private String dir;
    private String class_;
    private String title;
    private String id;
    private String style;
    private String lang;





    private xhtml_DlType xhtml_dltype;


    public xhtml_DdType(
        String lang1,        String dir,        String class_,        String title,        String id,        String style,        String lang    ) {
        super(
        );
        this.lang1 = lang1;
        this.dir = dir;
        this.class_ = class_;
        this.title = title;
        this.id = id;
        this.style = style;
        this.lang = lang;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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

    public xhtml_DlType getXhtml_dltype() {
        return xhtml_dltype;
    }

    public void setXhtml_dltype(xhtml_DlType xhtml_dltype) {
        this.xhtml_dltype = xhtml_dltype;
    }

}