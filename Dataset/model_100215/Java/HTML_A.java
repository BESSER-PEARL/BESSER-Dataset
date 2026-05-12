





import java.util.List;
import java.util.ArrayList;

public class HTML_A extends BODYElement {

    private String id;
    private String ahref;
    private String name;



    public HTML_A(
        String id,        String ahref,        String name    ) {
        super(
        );
        this.id = id;
        this.ahref = ahref;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}