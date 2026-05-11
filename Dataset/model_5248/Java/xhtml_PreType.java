





import java.util.List;
import java.util.ArrayList;

public class xhtml_PreType extends PreContent {

    private String class_;
    private String id;
    private String title;
    private String style;





    private xhtml_FormContent xhtml_formcontent;




    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_Flow xhtml_flow;


    public xhtml_PreType(
        String class_,        String id,        String title,        String style    ) {
        super(
        );
        this.class_ = class_;
        this.id = id;
        this.title = title;
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

    public xhtml_FormContent getXhtml_formcontent() {
        return xhtml_formcontent;
    }

    public void setXhtml_formcontent(xhtml_FormContent xhtml_formcontent) {
        this.xhtml_formcontent = xhtml_formcontent;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_Flow getXhtml_flow() {
        return xhtml_flow;
    }

    public void setXhtml_flow(xhtml_Flow xhtml_flow) {
        this.xhtml_flow = xhtml_flow;
    }

}