





import java.util.List;
import java.util.ArrayList;

public class HTML_LINK extends HEADElement {

    private String ahref;
    private String rel;
    private String title;
    private String type;



    public HTML_LINK(
        String ahref,        String rel,        String title,        String type    ) {
        super(
        );
        this.ahref = ahref;
        this.rel = rel;
        this.title = title;
        this.type = type;
    }


    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }
    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}