





import java.util.List;
import java.util.ArrayList;

public class xhtml_LiType extends Flow {

    private String class_;
    private String style;
    private String id;
    private String title;





    private xhtml_OlType xhtml_oltype;




    private xhtml_UlType xhtml_ultype;


    public xhtml_LiType(
        String class_,        String style,        String id,        String title    ) {
        super(
        );
        this.class_ = class_;
        this.style = style;
        this.id = id;
        this.title = title;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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