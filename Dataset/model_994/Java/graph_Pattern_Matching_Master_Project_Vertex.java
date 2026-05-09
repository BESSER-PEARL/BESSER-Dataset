





import java.util.List;
import java.util.ArrayList;

public class graph_Pattern_Matching_Master_Project_Vertex  {

    private String name;





    private graph_Pattern_Matching_Master_Project_Edge graph_pattern_matching_master_project_edge;




    private graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph;




    private graph_Pattern_Matching_Master_Project_Edge graph_pattern_matching_master_project_edge;




    private graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph;




    private List<graph_Pattern_Matching_Master_Project_Entry> graph_pattern_matching_master_project_entrys;


    public graph_Pattern_Matching_Master_Project_Vertex(
        String name    ) {
        this.name = name;
        this.graph_pattern_matching_master_project_entrys = new ArrayList<>();
    }

    public graph_Pattern_Matching_Master_Project_Vertex(
        String name        ArrayList<graph_Pattern_Matching_Master_Project_Entry> graph_pattern_matching_master_project_entrys    ) {
        this.name = name;
        this.graph_pattern_matching_master_project_entrys = graph_pattern_matching_master_project_entrys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graph_Pattern_Matching_Master_Project_Edge getGraph_pattern_matching_master_project_edge() {
        return graph_pattern_matching_master_project_edge;
    }

    public void setGraph_pattern_matching_master_project_edge(graph_Pattern_Matching_Master_Project_Edge graph_pattern_matching_master_project_edge) {
        this.graph_pattern_matching_master_project_edge = graph_pattern_matching_master_project_edge;
    }
    public graph_Pattern_Matching_Master_Project_Graph getGraph_pattern_matching_master_project_graph() {
        return graph_pattern_matching_master_project_graph;
    }

    public void setGraph_pattern_matching_master_project_graph(graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph) {
        this.graph_pattern_matching_master_project_graph = graph_pattern_matching_master_project_graph;
    }
    public graph_Pattern_Matching_Master_Project_Edge getGraph_pattern_matching_master_project_edge() {
        return graph_pattern_matching_master_project_edge;
    }

    public void setGraph_pattern_matching_master_project_edge(graph_Pattern_Matching_Master_Project_Edge graph_pattern_matching_master_project_edge) {
        this.graph_pattern_matching_master_project_edge = graph_pattern_matching_master_project_edge;
    }
    public graph_Pattern_Matching_Master_Project_Graph getGraph_pattern_matching_master_project_graph() {
        return graph_pattern_matching_master_project_graph;
    }

    public void setGraph_pattern_matching_master_project_graph(graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph) {
        this.graph_pattern_matching_master_project_graph = graph_pattern_matching_master_project_graph;
    }
    public List<graph_Pattern_Matching_Master_Project_Entry> getGraph_pattern_matching_master_project_entrys() {
        return graph_pattern_matching_master_project_entrys;
    }

    public void addGraph_pattern_matching_master_project_entry(Graph_pattern_matching_master_project_entry graph_pattern_matching_master_project_entry) {
        this.graph_pattern_matching_master_project_entrys.add(graph_pattern_matching_master_project_entry);
    }

}