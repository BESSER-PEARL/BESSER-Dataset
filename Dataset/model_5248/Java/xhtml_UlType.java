





import java.util.List;
import java.util.ArrayList;

public class xhtml_UlType  {

    private String title;
    private String class_;
    private String id;
    private String style;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_DocumentRoot xhtml_documentroot;




    private List<xhtml_LiType> xhtml_litypes;




    private xhtml_Block xhtml_block;




    private xhtml_Flow xhtml_flow;




    private xhtml_FormContent xhtml_formcontent;


    public xhtml_UlType(
        String title,        String class_,        String id,        String style    ) {
        this.title = title;
        this.class_ = class_;
        this.id = id;
        this.style = style;
        this.xhtml_litypes = new ArrayList<>();
    }

    public xhtml_UlType(
        String title,        String class_,        String id,        String style        ArrayList<xhtml_LiType> xhtml_litypes    ) {
        this.title = title;
        this.class_ = class_;
        this.id = id;
        this.style = style;
        this.xhtml_litypes = xhtml_litypes;
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

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public List<xhtml_LiType> getXhtml_litypes() {
        return xhtml_litypes;
    }

    public void addXhtml_litype(Xhtml_litype xhtml_litype) {
        this.xhtml_litypes.add(xhtml_litype);
    }
    public xhtml_Block getXhtml_block() {
        return xhtml_block;
    }

    public void setXhtml_block(xhtml_Block xhtml_block) {
        this.xhtml_block = xhtml_block;
    }
    public xhtml_Flow getXhtml_flow() {
        return xhtml_flow;
    }

    public void setXhtml_flow(xhtml_Flow xhtml_flow) {
        this.xhtml_flow = xhtml_flow;
    }
    public xhtml_FormContent getXhtml_formcontent() {
        return xhtml_formcontent;
    }

    public void setXhtml_formcontent(xhtml_FormContent xhtml_formcontent) {
        this.xhtml_formcontent = xhtml_formcontent;
    }

}