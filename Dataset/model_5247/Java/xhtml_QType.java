





import java.util.List;
import java.util.ArrayList;

public class xhtml_QType extends Inline {

    private String title;
    private String id;
    private String style;
    private String class_;
    private String cite1;



    public xhtml_QType(
        String title,        String id,        String style,        String class_,        String cite1    ) {
        super(
        );
        this.title = title;
        this.id = id;
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


}