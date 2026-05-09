





import java.util.List;
import java.util.ArrayList;

public class henshin_Graph extends NamedElement {






    private List<henshin_Node> henshin_nodes;




    private henshin_Formula henshin_formula;




    private henshin_Node henshin_node;




    private henshin_NestedCondition henshin_nestedcondition;




    private henshin_Rule henshin_rule;




    private henshin_Edge henshin_edge;




    private henshin_Rule henshin_rule;




    private List<henshin_Edge> henshin_edges;


    public henshin_Graph(
    ) {
        super(
        );
        this.henshin_nodes = new ArrayList<>();
        this.henshin_edges = new ArrayList<>();
    }

    public henshin_Graph(
        ArrayList<henshin_Node> henshin_nodes,        ArrayList<henshin_Edge> henshin_edges    ) {
        this.henshin_nodes = henshin_nodes;
        this.henshin_edges = henshin_edges;
    }


    public List<henshin_Node> getHenshin_nodes() {
        return henshin_nodes;
    }

    public void addHenshin_node(Henshin_node henshin_node) {
        this.henshin_nodes.add(henshin_node);
    }
    public henshin_Formula getHenshin_formula() {
        return henshin_formula;
    }

    public void setHenshin_formula(henshin_Formula henshin_formula) {
        this.henshin_formula = henshin_formula;
    }
    public henshin_Node getHenshin_node() {
        return henshin_node;
    }

    public void setHenshin_node(henshin_Node henshin_node) {
        this.henshin_node = henshin_node;
    }
    public henshin_NestedCondition getHenshin_nestedcondition() {
        return henshin_nestedcondition;
    }

    public void setHenshin_nestedcondition(henshin_NestedCondition henshin_nestedcondition) {
        this.henshin_nestedcondition = henshin_nestedcondition;
    }
    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }
    public henshin_Edge getHenshin_edge() {
        return henshin_edge;
    }

    public void setHenshin_edge(henshin_Edge henshin_edge) {
        this.henshin_edge = henshin_edge;
    }
    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }
    public List<henshin_Edge> getHenshin_edges() {
        return henshin_edges;
    }

    public void addHenshin_edge(Henshin_edge henshin_edge) {
        this.henshin_edges.add(henshin_edge);
    }

}