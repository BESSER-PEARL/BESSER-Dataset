





import java.util.List;
import java.util.ArrayList;

public class xhtml_DlType  {

    private String group;
    private String lang;
    private String title;
    private String class_;
    private String lang1;
    private String dir;
    private String style;
    private String id;





    private List<xhtml_DtType> xhtml_dttypes;




    private xhtml_MapType xhtml_maptype;




    private xhtml_Block xhtml_block;


    public xhtml_DlType(
        String group,        String lang,        String title,        String class_,        String lang1,        String dir,        String style,        String id    ) {
        this.group = group;
        this.lang = lang;
        this.title = title;
        this.class_ = class_;
        this.lang1 = lang1;
        this.dir = dir;
        this.style = style;
        this.id = id;
        this.xhtml_dttypes = new ArrayList<>();
    }

    public xhtml_DlType(
        String group,        String lang,        String title,        String class_,        String lang1,        String dir,        String style,        String id        ArrayList<xhtml_DtType> xhtml_dttypes    ) {
        this.group = group;
        this.lang = lang;
        this.title = title;
        this.class_ = class_;
        this.lang1 = lang1;
        this.dir = dir;
        this.style = style;
        this.id = id;
        this.xhtml_dttypes = xhtml_dttypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<xhtml_DtType> getXhtml_dttypes() {
        return xhtml_dttypes;
    }

    public void addXhtml_dttype(Xhtml_dttype xhtml_dttype) {
        this.xhtml_dttypes.add(xhtml_dttype);
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