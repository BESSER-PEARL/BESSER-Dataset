





import java.util.List;
import java.util.ArrayList;

public class build_IPathGroup  {

    private String basePath;
    private String paths;





    private build_IArtifactsPart build_iartifactspart;


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

    public build_IArtifactsPart getBuild_iartifactspart() {
        return build_iartifactspart;
    }

    public void setBuild_iartifactspart(build_IArtifactsPart build_iartifactspart) {
        this.build_iartifactspart = build_iartifactspart;
    }

}