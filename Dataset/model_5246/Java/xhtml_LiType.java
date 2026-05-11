





import java.util.List;
import java.util.ArrayList;

public class xhtml_LiType extends Flow {

    private String dir;
    private String title;
    private String style;
    private String class_;
    private String id;
    private String lang;
    private String lang1;





    private xhtml_OlType xhtml_oltype;




    private xhtml_UlType xhtml_ultype;


    public xhtml_LiType(
        String dir,        String title,        String style,        String class_,        String id,        String lang,        String lang1    ) {
        super(
        );
        this.dir = dir;
        this.title = title;
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.lang = lang;
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
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }

    public xhtml_OlType getXhtml_oltype() {
        return xhtml_oltype;
    }

    public void setXhtml_oltype(xhtml_OlType xhtml_oltype) {
        this.xhtml_oltype = xhtml_oltype;
    }
    public xhtml_UlType getXhtml_ultype() {
        return xhtml_ultype;
    }

    public void setXhtml_ultype(xhtml_UlType xhtml_ultype) {
        this.xhtml_ultype = xhtml_ultype;
    }

}