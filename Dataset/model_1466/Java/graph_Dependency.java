





import java.util.List;
import java.util.ArrayList;

public class graph_Dependency  {

    private String locality;
    private String id;



    public graph_Dependency(
        String locality,        String id    ) {
        this.locality = locality;
        this.id = id;
    }


    public String getLocality() {
        return locality;
    }

    public void setLocality(String locality) {
        this.locality = locality;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}