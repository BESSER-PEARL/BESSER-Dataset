





import java.util.List;
import java.util.ArrayList;

public class HTML_A extends BODYElement {

    private String id;
    private String name;
    private String ahref;



    public HTML_A(
        String id,        String name,        String ahref    ) {
        super(
        );
        this.id = id;
        this.name = name;
        this.ahref = ahref;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }


}