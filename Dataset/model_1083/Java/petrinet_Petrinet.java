





import java.util.List;
import java.util.ArrayList;

public class petrinet_Petrinet  {

    private String name;





    private petrinet_Node petrinet_node;




    private List<petrinet_Node> petrinet_nodes;


    public petrinet_Petrinet(
        String name    ) {
        this.name = name;
        this.petrinet_nodes = new ArrayList<>();
    }

    public petrinet_Petrinet(
        String name        ArrayList<petrinet_Node> petrinet_nodes    ) {
        this.name = name;
        this.petrinet_nodes = petrinet_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Node getPetrinet_node() {
        return petrinet_node;
    }

    public void setPetrinet_node(petrinet_Node petrinet_node) {
        this.petrinet_node = petrinet_node;
    }
    public List<petrinet_Node> getPetrinet_nodes() {
        return petrinet_nodes;
    }

    public void addPetrinet_node(Petrinet_node petrinet_node) {
        this.petrinet_nodes.add(petrinet_node);
    }

}