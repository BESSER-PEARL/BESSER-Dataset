





import java.util.List;
import java.util.ArrayList;

public class graph_Pattern_Matching_Master_Project_Edge  {

    private String label;





    private List<graph_Pattern_Matching_Master_Project_Entry> graph_pattern_matching_master_project_entrys;




    private graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph;




    private graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph;


    public graph_Pattern_Matching_Master_Project_Edge(
        String label    ) {
        this.label = label;
        this.graph_pattern_matching_master_project_entrys = new ArrayList<>();
    }

    public graph_Pattern_Matching_Master_Project_Edge(
        String label        ArrayList<graph_Pattern_Matching_Master_Project_Entry> graph_pattern_matching_master_project_entrys    ) {
        this.label = label;
        this.graph_pattern_matching_master_project_entrys = graph_pattern_matching_master_project_entrys;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<graph_Pattern_Matching_Master_Project_Entry> getGraph_pattern_matching_master_project_entrys() {
        return graph_pattern_matching_master_project_entrys;
    }

    public void addGraph_pattern_matching_master_project_entry(Graph_pattern_matching_master_project_entry graph_pattern_matching_master_project_entry) {
        this.graph_pattern_matching_master_project_entrys.add(graph_pattern_matching_master_project_entry);
    }
    public graph_Pattern_Matching_Master_Project_Graph getGraph_pattern_matching_master_project_graph() {
        return graph_pattern_matching_master_project_graph;
    }

    public void setGraph_pattern_matching_master_project_graph(graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph) {
        this.graph_pattern_matching_master_project_graph = graph_pattern_matching_master_project_graph;
    }
    public graph_Pattern_Matching_Master_Project_Graph getGraph_pattern_matching_master_project_graph() {
        return graph_pattern_matching_master_project_graph;
    }

    public void setGraph_pattern_matching_master_project_graph(graph_Pattern_Matching_Master_Project_Graph graph_pattern_matching_master_project_graph) {
        this.graph_pattern_matching_master_project_graph = graph_pattern_matching_master_project_graph;
    }

}