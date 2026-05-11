





import java.util.List;
import java.util.ArrayList;

public class xhtml_DlType  {

    private String style;
    private String class_;
    private String id;
    private String group;
    private String title;





    private xhtml_Flow xhtml_flow;




    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_FormContent xhtml_formcontent;




    private List<xhtml_DdType> xhtml_ddtypes;




    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_Block xhtml_block;




    private List<xhtml_DtType> xhtml_dttypes;


    public xhtml_DlType(
        String style,        String class_,        String id,        String group,        String title    ) {
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.group = group;
        this.title = title;
        this.xhtml_ddtypes = new ArrayList<>();
        this.xhtml_dttypes = new ArrayList<>();
    }

    public xhtml_DlType(
        String style,        String class_,        String id,        String group,        String title        ArrayList<xhtml_DdType> xhtml_ddtypes,        ArrayList<xhtml_DtType> xhtml_dttypes    ) {
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.group = group;
        this.title = title;
        this.xhtml_ddtypes = xhtml_ddtypes;
        this.xhtml_dttypes = xhtml_dttypes;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public xhtml_Flow getXhtml_flow() {
        return xhtml_flow;
    }

    public void setXhtml_flow(xhtml_Flow xhtml_flow) {
        this.xhtml_flow = xhtml_flow;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_FormContent getXhtml_formcontent() {
        return xhtml_formcontent;
    }

    public void setXhtml_formcontent(xhtml_FormContent xhtml_formcontent) {
        this.xhtml_formcontent = xhtml_formcontent;
    }
    public List<xhtml_DdType> getXhtml_ddtypes() {
        return xhtml_ddtypes;
    }

    public void addXhtml_ddtype(Xhtml_ddtype xhtml_ddtype) {
        this.xhtml_ddtypes.add(xhtml_ddtype);
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public List<xhtml_DtType> getXhtml_dttypes() {
        return xhtml_dttypes;
    }

    public void addXhtml_dttype(Xhtml_dttype xhtml_dttype) {
        this.xhtml_dttypes.add(xhtml_dttype);
    }

}