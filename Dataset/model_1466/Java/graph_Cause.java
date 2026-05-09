





import java.util.List;
import java.util.ArrayList;

public class graph_Cause  {

    private String type;
    private String version;
    private String name;





    private graph_Dependency graph_dependency;


    public graph_Cause(
        String type,        String version,        String name    ) {
        this.type = type;
        this.version = version;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graph_Dependency getGraph_dependency() {
        return graph_dependency;
    }

    public void setGraph_dependency(graph_Dependency graph_dependency) {
        this.graph_dependency = graph_dependency;
    }

}