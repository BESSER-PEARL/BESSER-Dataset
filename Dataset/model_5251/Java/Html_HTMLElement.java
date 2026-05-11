





import java.util.List;
import java.util.ArrayList;

public class Html_HTMLElement  {

    private String id;
    private String class_;
    private String title;
    private String value;



    public Html_HTMLElement(
        String id,        String class_,        String title,        String value    ) {
        this.id = id;
        this.class_ = class_;
        this.title = title;
        this.value = value;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}