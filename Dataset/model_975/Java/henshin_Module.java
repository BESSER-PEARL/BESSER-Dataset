





import java.util.List;
import java.util.ArrayList;

public class henshin_Module extends NamedElement {






    private List<henshin_Graph> henshin_graphs;




    private henshin_Module henshin_module;




    private henshin_Module henshin_module;


    public henshin_Module(
    ) {
        super(
        );
        this.henshin_graphs = new ArrayList<>();
    }

    public henshin_Module(
        ArrayList<henshin_Graph> henshin_graphs    ) {
        this.henshin_graphs = henshin_graphs;
    }


    public List<henshin_Graph> getHenshin_graphs() {
        return henshin_graphs;
    }

    public void addHenshin_graph(Henshin_graph henshin_graph) {
        this.henshin_graphs.add(henshin_graph);
    }
    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }
    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }

}