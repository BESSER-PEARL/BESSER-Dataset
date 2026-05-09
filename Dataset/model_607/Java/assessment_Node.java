





import java.util.List;
import java.util.ArrayList;

public class assessment_Node extends Label, Notes {






    private List<assessment_Node> assessment_nodes;




    private assessment_Node assessment_node;




    private List<assessment_GraphNode> assessment_graphnodes;




    private List<assessment_Node> assessment_nodes;


    public assessment_Node(
    ) {
        super(
        );
        this.assessment_nodes = new ArrayList<>();
        this.assessment_graphnodes = new ArrayList<>();
        this.assessment_nodes = new ArrayList<>();
    }

    public assessment_Node(
        ArrayList<assessment_Node> assessment_nodes,        ArrayList<assessment_GraphNode> assessment_graphnodes,        ArrayList<assessment_Node> assessment_nodes    ) {
        this.assessment_nodes = assessment_nodes;
        this.assessment_graphnodes = assessment_graphnodes;
        this.assessment_nodes = assessment_nodes;
    }


    public List<assessment_Node> getAssessment_nodes() {
        return assessment_nodes;
    }

    public void addAssessment_node(Assessment_node assessment_node) {
        this.assessment_nodes.add(assessment_node);
    }
    public assessment_Node getAssessment_node() {
        return assessment_node;
    }

    public void setAssessment_node(assessment_Node assessment_node) {
        this.assessment_node = assessment_node;
    }
    public List<assessment_GraphNode> getAssessment_graphnodes() {
        return assessment_graphnodes;
    }

    public void addAssessment_graphnode(Assessment_graphnode assessment_graphnode) {
        this.assessment_graphnodes.add(assessment_graphnode);
    }
    public List<assessment_Node> getAssessment_nodes() {
        return assessment_nodes;
    }

    public void addAssessment_node(Assessment_node assessment_node) {
        this.assessment_nodes.add(assessment_node);
    }

}