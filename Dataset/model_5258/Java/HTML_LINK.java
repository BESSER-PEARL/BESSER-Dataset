





import java.util.List;
import java.util.ArrayList;

public class HTML_LINK extends HEADElement {

    private String title;
    private String rel;
    private String ahref;
    private String type;



    public HTML_LINK(
        String title,        String rel,        String ahref,        String type    ) {
        super(
        );
        this.title = title;
        this.rel = rel;
        this.ahref = ahref;
        this.type = type;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}