





import java.util.List;
import java.util.ArrayList;

public class build_Platform  {

    private String file;
    private String location;
    private String deltapack;



    public build_Platform(
        String file,        String location,        String deltapack    ) {
        this.file = file;
        this.location = location;
        this.deltapack = deltapack;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getDeltapack() {
        return deltapack;
    }

    public void setDeltapack(String deltapack) {
        this.deltapack = deltapack;
    }


}