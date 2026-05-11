





import java.util.List;
import java.util.ArrayList;

public class xhtml_DelType extends Flow {

    private String datetime;
    private String class_;
    private String title;
    private String cite1;
    private String id;
    private String style;





    private xhtml_AContent xhtml_acontent;




    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_DelType(
        String datetime,        String class_,        String title,        String cite1,        String id,        String style    ) {
        super(
        );
        this.datetime = datetime;
        this.class_ = class_;
        this.title = title;
        this.cite1 = cite1;
        this.id = id;
        this.style = style;
    }


    public String getDatetime() {
        return datetime;
    }

    public void setDatetime(String datetime) {
        this.datetime = datetime;
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
    public String getCite1() {
        return cite1;
    }

    public void setCite1(String cite1) {
        this.cite1 = cite1;
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