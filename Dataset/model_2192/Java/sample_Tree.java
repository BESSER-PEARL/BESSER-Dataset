





import java.util.List;
import java.util.ArrayList;

public class sample_Tree  {

    private String name;





    private sample_Tree sample_tree;




    private sample_Tree sample_tree;




    private List<sample_Comment> sample_comments;




    private sample_Node sample_node;




    private List<sample_Node> sample_nodes;


    public sample_Tree(
        String name    ) {
        this.name = name;
        this.sample_comments = new ArrayList<>();
        this.sample_nodes = new ArrayList<>();
    }

    public sample_Tree(
        String name        ArrayList<sample_Comment> sample_comments,        ArrayList<sample_Node> sample_nodes    ) {
        this.name = name;
        this.sample_comments = sample_comments;
        this.sample_nodes = sample_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sample_Tree getSample_tree() {
        return sample_tree;
    }

    public void setSample_tree(sample_Tree sample_tree) {
        this.sample_tree = sample_tree;
    }
    public sample_Tree getSample_tree() {
        return sample_tree;
    }

    public void setSample_tree(sample_Tree sample_tree) {
        this.sample_tree = sample_tree;
    }
    public List<sample_Comment> getSample_comments() {
        return sample_comments;
    }

    public void addSample_comment(Sample_comment sample_comment) {
        this.sample_comments.add(sample_comment);
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