





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DResource  {

    private String name;
    private String path;



    public viewpoint_DResource(
        String name,        String path    ) {
        this.name = name;
        this.path = path;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}