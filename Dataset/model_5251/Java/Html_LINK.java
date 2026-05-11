





import java.util.List;
import java.util.ArrayList;

public class Html_LINK extends HEADElement {

    private String type;
    private String rel;
    private String ahref;



    public Html_LINK(
        String type,        String rel,        String ahref    ) {
        super(
        );
        this.type = type;
        this.rel = rel;
        this.ahref = ahref;
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