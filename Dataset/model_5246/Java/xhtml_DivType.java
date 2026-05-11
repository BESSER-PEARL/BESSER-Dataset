





import java.util.List;
import java.util.ArrayList;

public class xhtml_DivType extends Flow {

    private String style;
    private String lang;
    private String lang1;
    private String id;
    private String title;
    private String dir;
    private String class_;





    private xhtml_MapType xhtml_maptype;




    private xhtml_Block xhtml_block;


    public xhtml_DivType(
        String style,        String lang,        String lang1,        String id,        String title,        String dir,        String class_    ) {
        super(
        );
        this.style = style;
        this.lang = lang;
        this.lang1 = lang1;
        this.id = id;
        this.title = title;
        this.dir = dir;
        this.class_ = class_;
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

    public xhtml_MapType getXhtml_maptype() {
        return xhtml_maptype;
    }

    public void setXhtml_maptype(xhtml_MapType xhtml_maptype) {
        this.xhtml_maptype = xhtml_maptype;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}