





import java.util.List;
import java.util.ArrayList;

public class xhtml_H2Type extends Inline {

    private String title;
    private String style;
    private String id;
    private String class_;



    public xhtml_H2Type(
        String title,        String style,        String id,        String class_    ) {
        super(
        );
        this.title = title;
        this.style = style;
        this.id = id;
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


}