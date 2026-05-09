





import java.util.List;
import java.util.ArrayList;

public class henshin_NestedCondition extends Formula {

    private String presenceCondition;





    private List<henshin_Mapping> henshin_mappings;




    private henshin_Graph henshin_graph;


    public henshin_NestedCondition(
        String presenceCondition    ) {
        super(
        );
        this.presenceCondition = presenceCondition;
        this.henshin_mappings = new ArrayList<>();
    }

    public henshin_NestedCondition(
        String presenceCondition        ArrayList<henshin_Mapping> henshin_mappings    ) {
        this.presenceCondition = presenceCondition;
        this.henshin_mappings = henshin_mappings;
    }

    public String getPresencecondition() {
        return presenceCondition;
    }

    public void setPresencecondition(String presenceCondition) {
        this.presenceCondition = presenceCondition;
    }

    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }

}