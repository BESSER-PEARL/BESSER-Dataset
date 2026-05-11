





import java.util.List;
import java.util.ArrayList;

public class xhtml_DtType extends Inline {

    private String class_;
    private String style;
    private String id;
    private String title;



    public xhtml_DtType(
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


}