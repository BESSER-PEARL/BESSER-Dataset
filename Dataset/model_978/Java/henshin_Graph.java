





import java.util.List;
import java.util.ArrayList;

public class henshin_Graph extends NamedElement {






    private henshin_Module henshin_module;




    private List<henshin_Node> henshin_nodes;




    private henshin_Node henshin_node;


    public henshin_Graph(
    ) {
        super(
        );
        this.henshin_nodes = new ArrayList<>();
    }

    public henshin_Graph(
        ArrayList<henshin_Node> henshin_nodes    ) {
        this.henshin_nodes = henshin_nodes;
    }


    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }
    public List<henshin_Node> getHenshin_nodes() {
        return henshin_nodes;
    }

    public void addHenshin_node(Henshin_node henshin_node) {
        this.henshin_nodes.add(henshin_node);
    }
    public henshin_Node getHenshin_node() {
        return henshin_node;
    }

    public void setHenshin_node(henshin_Node henshin_node) {
        this.henshin_node = henshin_node;
    }

}