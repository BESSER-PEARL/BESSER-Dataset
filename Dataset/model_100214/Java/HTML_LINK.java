





import java.util.List;
import java.util.ArrayList;

public class HTML_LINK extends HEADElement {

    private String ahref;
    private String type;
    private String title;
    private String rel;



    public HTML_LINK(
        String ahref,        String type,        String title,        String rel    ) {
        super(
        );
        this.ahref = ahref;
        this.type = type;
        this.title = title;
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


}