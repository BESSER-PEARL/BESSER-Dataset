





import java.util.List;
import java.util.ArrayList;

public class html_LINK extends HEADElement {

    private String title;
    private String type;
    private String rel;
    private String ahref;



    public html_LINK(
        String title,        String type,        String rel,        String ahref    ) {
        super(
        );
        this.title = title;
        this.type = type;
        this.rel = rel;
        this.ahref = ahref;
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


}