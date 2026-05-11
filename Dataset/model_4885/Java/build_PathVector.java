





import java.util.List;
import java.util.ArrayList;

public class build_PathVector  {

    private String paths;
    private String basePath;





    private build_ConditionalPathVector build_conditionalpathvector;


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

    public build_ConditionalPathVector getBuild_conditionalpathvector() {
        return build_conditionalpathvector;
    }

    public void setBuild_conditionalpathvector(build_ConditionalPathVector build_conditionalpathvector) {
        this.build_conditionalpathvector = build_conditionalpathvector;
    }

}