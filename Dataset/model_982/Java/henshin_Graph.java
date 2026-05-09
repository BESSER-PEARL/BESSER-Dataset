





import java.util.List;
import java.util.ArrayList;

public class henshin_Graph extends NamedElement {






    private List<henshin_Node> henshin_nodes;




    private henshin_Node henshin_node;




    private henshin_TransformationSystem henshin_transformationsystem;


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
    public henshin_TransformationSystem getHenshin_transformationsystem() {
        return henshin_transformationsystem;
    }

    public void setHenshin_transformationsystem(henshin_TransformationSystem henshin_transformationsystem) {
        this.henshin_transformationsystem = henshin_transformationsystem;
    }

}