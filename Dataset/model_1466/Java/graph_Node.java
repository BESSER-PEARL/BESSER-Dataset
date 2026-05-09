





import java.util.List;
import java.util.ArrayList;

public class graph_Node  {

    private String nodeName;
    private String unitName;
    private String id;
    private String containerName;
    private String unitVersion;





    private List<graph_Dependency> graph_dependencys;




    private graph_Dependency graph_dependency;




    private graph_Dependency graph_dependency;




    private List<graph_Dependency> graph_dependencys;


    public graph_Node(
        String nodeName,        String unitName,        String id,        String containerName,        String unitVersion    ) {
        this.nodeName = nodeName;
        this.unitName = unitName;
        this.id = id;
        this.containerName = containerName;
        this.unitVersion = unitVersion;
        this.graph_dependencys = new ArrayList<>();
        this.graph_dependencys = new ArrayList<>();
    }

    public graph_Node(
        String nodeName,        String unitName,        String id,        String containerName,        String unitVersion        ArrayList<graph_Dependency> graph_dependencys,        ArrayList<graph_Dependency> graph_dependencys    ) {
        this.nodeName = nodeName;
        this.unitName = unitName;
        this.id = id;
        this.containerName = containerName;
        this.unitVersion = unitVersion;
        this.graph_dependencys = graph_dependencys;
        this.graph_dependencys = graph_dependencys;
    }

    public String getNodename() {
        return nodeName;
    }

    public void setNodename(String nodeName) {
        this.nodeName = nodeName;
    }
    public String getUnitname() {
        return unitName;
    }

    public void setUnitname(String unitName) {
        this.unitName = unitName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getContainername() {
        return containerName;
    }

    public void setContainername(String containerName) {
        this.containerName = containerName;
    }
    public String getUnitversion() {
        return unitVersion;
    }

    public void setUnitversion(String unitVersion) {
        this.unitVersion = unitVersion;
    }

    public List<graph_Dependency> getGraph_dependencys() {
        return graph_dependencys;
    }

    public void addGraph_dependency(Graph_dependency graph_dependency) {
        this.graph_dependencys.add(graph_dependency);
    }
    public graph_Dependency getGraph_dependency() {
        return graph_dependency;
    }

    public void setGraph_dependency(graph_Dependency graph_dependency) {
        this.graph_dependency = graph_dependency;
    }
    public graph_Dependency getGraph_dependency() {
        return graph_dependency;
    }

    public void setGraph_dependency(graph_Dependency graph_dependency) {
        this.graph_dependency = graph_dependency;
    }
    public List<graph_Dependency> getGraph_dependencys() {
        return graph_dependencys;
    }

    public void addGraph_dependency(Graph_dependency graph_dependency) {
        this.graph_dependencys.add(graph_dependency);
    }

}