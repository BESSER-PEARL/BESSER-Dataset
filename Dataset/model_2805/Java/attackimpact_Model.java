





import java.util.List;
import java.util.ArrayList;

public class attackimpact_Model  {

    private String description;
    private String name;





    private List<attackimpact_Node> attackimpact_nodes;


    public attackimpact_Model(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.attackimpact_nodes = new ArrayList<>();
    }

    public attackimpact_Model(
        String description,        String name        ArrayList<attackimpact_Node> attackimpact_nodes    ) {
        this.description = description;
        this.name = name;
        this.attackimpact_nodes = attackimpact_nodes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<attackimpact_Node> getAttackimpact_nodes() {
        return attackimpact_nodes;
    }

    public void addAttackimpact_node(Attackimpact_node attackimpact_node) {
        this.attackimpact_nodes.add(attackimpact_node);
    }

}