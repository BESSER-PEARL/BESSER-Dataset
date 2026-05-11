





import java.util.List;
import java.util.ArrayList;

public class p2_IVersionedId  {

    private String version;
    private String id;



    public p2_IVersionedId(
        String version,        String id    ) {
        this.version = version;
        this.id = id;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}