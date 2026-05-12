





import java.util.List;
import java.util.ArrayList;

public class setup_ApiBaselineTask extends SetupTask {

    private String version;
    private String zipLocation;
    private String containerFolder;



    public setup_ApiBaselineTask(
        String version,        String zipLocation,        String containerFolder    ) {
        super(
        );
        this.version = version;
        this.zipLocation = zipLocation;
        this.containerFolder = containerFolder;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getZiplocation() {
        return zipLocation;
    }

    public void setZiplocation(String zipLocation) {
        this.zipLocation = zipLocation;
    }
    public String getContainerfolder() {
        return containerFolder;
    }

    public void setContainerfolder(String containerFolder) {
        this.containerFolder = containerFolder;
    }


}