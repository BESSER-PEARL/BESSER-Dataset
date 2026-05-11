





import java.util.List;
import java.util.ArrayList;

public class xhtml_DlType  {

    private String id;
    private String class_;
    private String group;
    private String style;
    private String title;





    private xhtml_ObjectType xhtml_objecttype;




    private List<xhtml_DtType> xhtml_dttypes;




    private xhtml_Block xhtml_block;


    public xhtml_DlType(
        String id,        String class_,        String group,        String style,        String title    ) {
        this.id = id;
        this.class_ = class_;
        this.group = group;
        this.style = style;
        this.title = title;
        this.xhtml_dttypes = new ArrayList<>();
    }

    public xhtml_DlType(
        String id,        String class_,        String group,        String style,        String title        ArrayList<xhtml_DtType> xhtml_dttypes    ) {
        this.id = id;
        this.class_ = class_;
        this.group = group;
        this.style = style;
        this.title = title;
        this.xhtml_dttypes = xhtml_dttypes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
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

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public List<xhtml_DtType> getXhtml_dttypes() {
        return xhtml_dttypes;
    }

    public void addXhtml_dttype(Xhtml_dttype xhtml_dttype) {
        this.xhtml_dttypes.add(xhtml_dttype);
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }

}