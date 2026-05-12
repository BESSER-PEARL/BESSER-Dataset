





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_PathElement extends Basic {

    private String location;
    private String path;





    private MavenMaven_Path mavenmaven_path;


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

    public MavenMaven_Path getMavenmaven_path() {
        return mavenmaven_path;
    }

    public void setMavenmaven_path(MavenMaven_Path mavenmaven_path) {
        this.mavenmaven_path = mavenmaven_path;
    }

}