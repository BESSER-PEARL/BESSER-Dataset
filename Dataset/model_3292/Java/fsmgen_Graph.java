





import java.util.List;
import java.util.ArrayList;

public class fsmgen_Graph extends FSMGenElement {






    private List<fsmgen_Link> fsmgen_links;




    private fsmgen_Link fsmgen_link;




    private fsmgen_Node fsmgen_node;




    private fsmgen_Node fsmgen_node;




    private fsmgen_GraphContainer fsmgen_graphcontainer;




    private List<fsmgen_Node> fsmgen_nodes;




    private fsmgen_Node fsmgen_node;




    private fsmgen_StateGraph fsmgen_stategraph;


    public fsmgen_Graph(
    ) {
        super(
        );
        this.fsmgen_links = new ArrayList<>();
        this.fsmgen_nodes = new ArrayList<>();
    }

    public fsmgen_Graph(
        ArrayList<fsmgen_Link> fsmgen_links,        ArrayList<fsmgen_Node> fsmgen_nodes    ) {
        this.fsmgen_links = fsmgen_links;
        this.fsmgen_nodes = fsmgen_nodes;
    }


    public List<fsmgen_Link> getFsmgen_links() {
        return fsmgen_links;
    }

    public void addFsmgen_link(Fsmgen_link fsmgen_link) {
        this.fsmgen_links.add(fsmgen_link);
    }
    public fsmgen_Link getFsmgen_link() {
        return fsmgen_link;
    }

    public void setFsmgen_link(fsmgen_Link fsmgen_link) {
        this.fsmgen_link = fsmgen_link;
    }
    public fsmgen_Node getFsmgen_node() {
        return fsmgen_node;
    }

    public void setFsmgen_node(fsmgen_Node fsmgen_node) {
        this.fsmgen_node = fsmgen_node;
    }
    public fsmgen_Node getFsmgen_node() {
        return fsmgen_node;
    }

    public void setFsmgen_node(fsmgen_Node fsmgen_node) {
        this.fsmgen_node = fsmgen_node;
    }
    public fsmgen_GraphContainer getFsmgen_graphcontainer() {
        return fsmgen_graphcontainer;
    }

    public void setFsmgen_graphcontainer(fsmgen_GraphContainer fsmgen_graphcontainer) {
        this.fsmgen_graphcontainer = fsmgen_graphcontainer;
    }
    public List<fsmgen_Node> getFsmgen_nodes() {
        return fsmgen_nodes;
    }

    public void addFsmgen_node(Fsmgen_node fsmgen_node) {
        this.fsmgen_nodes.add(fsmgen_node);
    }
    public fsmgen_Node getFsmgen_node() {
        return fsmgen_node;
    }

    public void setFsmgen_node(fsmgen_Node fsmgen_node) {
        this.fsmgen_node = fsmgen_node;
    }
    public fsmgen_StateGraph getFsmgen_stategraph() {
        return fsmgen_stategraph;
    }

    public void setFsmgen_stategraph(fsmgen_StateGraph fsmgen_stategraph) {
        this.fsmgen_stategraph = fsmgen_stategraph;
    }

}