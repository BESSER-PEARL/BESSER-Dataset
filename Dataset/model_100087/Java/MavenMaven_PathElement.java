





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_PathElement extends Basic {

    private String location;
    private String path;



    public MavenMaven_PathElement(
        String location,        String path    ) {
        super(
        );
        this.location = location;
        this.path = path;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}