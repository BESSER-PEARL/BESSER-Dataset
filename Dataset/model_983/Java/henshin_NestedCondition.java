





import java.util.List;
import java.util.ArrayList;

public class henshin_NestedCondition extends Formula {






    private henshin_Graph henshin_graph;




    private List<henshin_Mapping> henshin_mappings;


    public henshin_NestedCondition(
    ) {
        super(
        );
        this.henshin_mappings = new ArrayList<>();
    }

    public henshin_NestedCondition(
        ArrayList<henshin_Mapping> henshin_mappings    ) {
        this.henshin_mappings = henshin_mappings;
    }


    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }

}