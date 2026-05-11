





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DResource  {

    private String path;
    private String name;



    public viewpoint_DResource(
        String path,        String name    ) {
        this.path = path;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}