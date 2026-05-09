





import java.util.List;
import java.util.ArrayList;

public class henshin_Graph extends NamedElement {






    private henshin_Edge henshin_edge;




    private List<henshin_Edge> henshin_edges;




    private henshin_NestedCondition henshin_nestedcondition;


    public henshin_Graph(
    ) {
        super(
        );
        this.henshin_edges = new ArrayList<>();
    }

    public henshin_Graph(
        ArrayList<henshin_Edge> henshin_edges    ) {
        this.henshin_edges = henshin_edges;
    }


    public henshin_Edge getHenshin_edge() {
        return henshin_edge;
    }

    public void setHenshin_edge(henshin_Edge henshin_edge) {
        this.henshin_edge = henshin_edge;
    }
    public List<henshin_Edge> getHenshin_edges() {
        return henshin_edges;
    }

    public void addHenshin_edge(Henshin_edge henshin_edge) {
        this.henshin_edges.add(henshin_edge);
    }
    public henshin_NestedCondition getHenshin_nestedcondition() {
        return henshin_nestedcondition;
    }

    public void setHenshin_nestedcondition(henshin_NestedCondition henshin_nestedcondition) {
        this.henshin_nestedcondition = henshin_nestedcondition;
    }

}