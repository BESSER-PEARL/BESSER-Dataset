





import java.util.List;
import java.util.ArrayList;

public class xhtml_H4Type extends Inline {

    private String title;
    private String style;
    private String class_;
    private String id;



    public xhtml_H4Type(
        String title,        String style,        String class_,        String id    ) {
        super(
        );
        this.title = title;
        this.style = style;
        this.class_ = class_;
        this.id = id;
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


}