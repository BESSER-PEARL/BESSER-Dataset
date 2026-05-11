





import java.util.List;
import java.util.ArrayList;

public class xhtml_QType extends Inline {

    private String style;
    private String cite1;
    private String id;
    private String title;
    private String class_;



    public xhtml_QType(
        String style,        String cite1,        String id,        String title,        String class_    ) {
        super(
        );
        this.style = style;
        this.cite1 = cite1;
        this.id = id;
        this.title = title;
        this.class_ = class_;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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


}