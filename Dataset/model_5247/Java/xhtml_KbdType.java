





import java.util.List;
import java.util.ArrayList;

public class xhtml_KbdType extends Inline {

    private String id;
    private String class_;
    private String title;
    private String style;



    public xhtml_KbdType(
        String id,        String class_,        String title,        String style    ) {
        super(
        );
        this.id = id;
        this.class_ = class_;
        this.title = title;
        this.style = style;
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


}