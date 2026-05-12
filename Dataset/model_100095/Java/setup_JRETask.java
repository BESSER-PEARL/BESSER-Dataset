





import java.util.List;
import java.util.ArrayList;

public class setup_JRETask extends SetupTask {

    private String version;
    private String location;



    public setup_JRETask(
        String version,        String location    ) {
        super(
        );
        this.version = version;
        this.location = location;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}