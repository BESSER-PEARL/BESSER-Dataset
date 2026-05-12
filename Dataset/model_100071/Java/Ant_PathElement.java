





import java.util.List;
import java.util.ArrayList;

public class Ant_PathElement extends Basic {

    private String location;
    private String path;





    private Ant_Path ant_path;


    public Ant_PathElement(
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

    public Ant_Path getAnt_path() {
        return ant_path;
    }

    public void setAnt_path(Ant_Path ant_path) {
        this.ant_path = ant_path;
    }

}