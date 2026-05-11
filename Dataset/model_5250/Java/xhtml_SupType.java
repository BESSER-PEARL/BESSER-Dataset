





import java.util.List;
import java.util.ArrayList;

public class xhtml_SupType extends Inline {

    private String style;
    private String class_;
    private String id;
    private String title;



    public xhtml_SupType(
        String style,        String class_,        String id,        String title    ) {
        super(
        );
        this.style = style;
        this.class_ = class_;
        this.id = id;
        this.title = title;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}