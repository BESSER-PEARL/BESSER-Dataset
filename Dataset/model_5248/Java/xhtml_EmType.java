





import java.util.List;
import java.util.ArrayList;

public class xhtml_EmType extends Inline {

    private String id;
    private String class_;
    private String style;
    private String title;



    public xhtml_EmType(
        String id,        String class_,        String style,        String title    ) {
        super(
        );
        this.id = id;
        this.class_ = class_;
        this.style = style;
        this.title = title;
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


}