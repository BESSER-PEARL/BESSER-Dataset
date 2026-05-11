





import java.util.List;
import java.util.ArrayList;

public class xhtml_UlType  {

    private String id;
    private String dir;
    private String lang1;
    private String title;
    private String class_;
    private String lang;
    private String style;





    private xhtml_Block xhtml_block;




    private xhtml_MapType xhtml_maptype;


    public xhtml_UlType(
        String id,        String dir,        String lang1,        String title,        String class_,        String lang,        String style    ) {
        this.id = id;
        this.dir = dir;
        this.lang1 = lang1;
        this.title = title;
        this.class_ = class_;
        this.lang = lang;
        this.style = style;
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
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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

    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_MapType getXhtml_maptype() {
        return xhtml_maptype;
    }

    public void setXhtml_maptype(xhtml_MapType xhtml_maptype) {
        this.xhtml_maptype = xhtml_maptype;
    }

}