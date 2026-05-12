





import java.util.List;
import java.util.ArrayList;

public class build_PathVector  {

    private String paths;
    private String basePath;



    public build_PathVector(
        String paths,        String basePath    ) {
        this.paths = paths;
        this.basePath = basePath;
    }


    public String getPaths() {
        return paths;
    }

    public void setPaths(String paths) {
        this.paths = paths;
    }
    public String getBasepath() {
        return basePath;
    }

    public void setBasepath(String basePath) {
        this.basePath = basePath;
    }


}