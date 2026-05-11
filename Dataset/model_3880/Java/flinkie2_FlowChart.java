





import java.util.List;
import java.util.ArrayList;

public class flinkie2_FlowChart  {






    private flinkie2_Init flinkie2_init;




    private List<flinkie2_Node> flinkie2_nodes;


    public flinkie2_FlowChart(
    ) {
        this.flinkie2_nodes = new ArrayList<>();
    }

    public flinkie2_FlowChart(
        ArrayList<flinkie2_Node> flinkie2_nodes    ) {
        this.flinkie2_nodes = flinkie2_nodes;
    }


    public flinkie2_Init getFlinkie2_init() {
        return flinkie2_init;
    }

    public void setFlinkie2_init(flinkie2_Init flinkie2_init) {
        this.flinkie2_init = flinkie2_init;
    }
    public List<flinkie2_Node> getFlinkie2_nodes() {
        return flinkie2_nodes;
    }

    public void addFlinkie2_node(Flinkie2_node flinkie2_node) {
        this.flinkie2_nodes.add(flinkie2_node);
    }

}