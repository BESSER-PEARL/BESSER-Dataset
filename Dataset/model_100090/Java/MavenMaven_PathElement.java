





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_PathElement extends Basic {

    private String path;
    private String location;



    public MavenMaven_PathElement(
        String path,        String location    ) {
        super(
        );
        this.path = path;
        this.location = location;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}