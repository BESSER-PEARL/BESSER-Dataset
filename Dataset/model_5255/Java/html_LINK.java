





import java.util.List;
import java.util.ArrayList;

public class html_LINK extends HEADElement {

    private String title;
    private String ahref;
    private String rel;
    private String type;



    public html_LINK(
        String title,        String ahref,        String rel,        String type    ) {
        super(
        );
        this.title = title;
        this.ahref = ahref;
        this.rel = rel;
        this.type = type;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}