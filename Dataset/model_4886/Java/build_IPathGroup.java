





import java.util.List;
import java.util.ArrayList;

public class build_IPathGroup  {

    private String basePath;
    private String paths;



    public build_IPathGroup(
        String basePath,        String paths    ) {
        this.basePath = basePath;
        this.paths = paths;
    }


    public String getBasepath() {
        return basePath;
    }

    public void setBasepath(String basePath) {
        this.basePath = basePath;
    }
    public String getPaths() {
        return paths;
    }

    public void setPaths(String paths) {
        this.paths = paths;
    }


}