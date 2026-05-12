





import java.util.List;
import java.util.ArrayList;

public class WikiTable_Table extends LocatedElement {

    private String style;
    private String class_;
    private String border;



    public WikiTable_Table(
        String style,        String class_,        String border    ) {
        super(
        );
        this.style = style;
        this.class_ = class_;
        this.border = border;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }


}