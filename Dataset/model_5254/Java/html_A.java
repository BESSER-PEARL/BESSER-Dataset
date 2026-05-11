





import java.util.List;
import java.util.ArrayList;

public class html_A extends BODYElement {

    private String ahref;
    private String name;
    private String id;



    public html_A(
        String ahref,        String name,        String id    ) {
        super(
        );
        this.ahref = ahref;
        this.name = name;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}