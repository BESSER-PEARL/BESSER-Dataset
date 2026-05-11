





import java.util.List;
import java.util.ArrayList;

public class xhtml_DelType extends Flow {

    private String title;
    private String id;
    private String datetime;
    private String style;
    private String class_;
    private String cite1;





    private xhtml_AContent xhtml_acontent;




    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_DelType(
        String title,        String id,        String datetime,        String style,        String class_,        String cite1    ) {
        super(
        );
        this.title = title;
        this.id = id;
        this.datetime = datetime;
        this.style = style;
        this.class_ = class_;
        this.cite1 = cite1;
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
    public String getDatetime() {
        return datetime;
    }

    public void setDatetime(String datetime) {
        this.datetime = datetime;
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
    public String getCite1() {
        return cite1;
    }

    public void setCite1(String cite1) {
        this.cite1 = cite1;
    }

    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}