





import java.util.List;
import java.util.ArrayList;

public class graph_ResourceGraph  {

    private String name;





    private graph_ResourceGraphs graph_resourcegraphs;


    public graph_ResourceGraph(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graph_ResourceGraphs getGraph_resourcegraphs() {
        return graph_resourcegraphs;
    }

    public void setGraph_resourcegraphs(graph_ResourceGraphs graph_resourcegraphs) {
        this.graph_resourcegraphs = graph_resourcegraphs;
    }

}