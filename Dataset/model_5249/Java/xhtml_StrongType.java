





import java.util.List;
import java.util.ArrayList;

public class xhtml_StrongType extends Inline {

    private String style;
    private String class_;
    private String title;
    private String id;



    public xhtml_StrongType(
        String style,        String class_,        String title,        String id    ) {
        super(
        );
        this.style = style;
        this.class_ = class_;
        this.title = title;
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


}