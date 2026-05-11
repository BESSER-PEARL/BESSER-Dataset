





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ITouchpointType  {

    private String version;
    private String id;



    public aggregator_p2_ITouchpointType(
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