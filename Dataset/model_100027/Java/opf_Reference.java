





import java.util.List;
import java.util.ArrayList;

public class opf_Reference  {

    private String type;
    private String title;
    private String href;



    public opf_Reference(
        String type,        String title,        String href    ) {
        this.type = type;
        this.title = title;
        this.href = href;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }


}