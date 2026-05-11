





import java.util.List;
import java.util.ArrayList;

public class sample_Node  {

    private String label;





    private sample_Node sample_node;




    private sample_Node sample_node;




    private sample_Node sample_node;




    private List<sample_Node> sample_nodes;


    public sample_Node(
        String label    ) {
        this.label = label;
        this.sample_nodes = new ArrayList<>();
    }

    public sample_Node(
        String label        ArrayList<sample_Node> sample_nodes    ) {
        this.label = label;
        this.sample_nodes = sample_nodes;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public sample_Node getSample_node() {
        return sample_node;
    }

    public void setSample_node(sample_Node sample_node) {
        this.sample_node = sample_node;
    }
    public sample_Node getSample_node() {
        return sample_node;
    }

    public void setSample_node(sample_Node sample_node) {
        this.sample_node = sample_node;
    }
    public sample_Node getSample_node() {
        return sample_node;
    }

    public void setSample_node(sample_Node sample_node) {
        this.sample_node = sample_node;
    }
    public List<sample_Node> getSample_nodes() {
        return sample_nodes;
    }

    public void addSample_node(Sample_node sample_node) {
        this.sample_nodes.add(sample_node);
    }

}