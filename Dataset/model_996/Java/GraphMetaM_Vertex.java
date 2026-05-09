





import java.util.List;
import java.util.ArrayList;

public class GraphMetaM_Vertex  {

    private String type;
    private String activity;
    private String rName;
    private int globalPriority;
    private String name;
    private int cycles;





    private GraphMetaM_Graph graphmetam_graph;


    public GraphMetaM_Vertex(
        String type,        String activity,        String rName,        int globalPriority,        String name,        int cycles    ) {
        this.type = type;
        this.activity = activity;
        this.rName = rName;
        this.globalPriority = globalPriority;
        this.name = name;
        this.cycles = cycles;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getRname() {
        return rName;
    }

    public void setRname(String rName) {
        this.rName = rName;
    }
    public int getGlobalpriority() {
        return globalPriority;
    }

    public void setGlobalpriority(int globalPriority) {
        this.globalPriority = globalPriority;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCycles() {
        return cycles;
    }

    public void setCycles(int cycles) {
        this.cycles = cycles;
    }

    public GraphMetaM_Graph getGraphmetam_graph() {
        return graphmetam_graph;
    }

    public void setGraphmetam_graph(GraphMetaM_Graph graphmetam_graph) {
        this.graphmetam_graph = graphmetam_graph;
    }

}