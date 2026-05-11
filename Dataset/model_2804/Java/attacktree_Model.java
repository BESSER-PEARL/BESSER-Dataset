





import java.util.List;
import java.util.ArrayList;

public class attacktree_Model  {

    private String description;
    private String name;





    private attacktree_Node attacktree_node;


    public attacktree_Model(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
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

    public attacktree_Node getAttacktree_node() {
        return attacktree_node;
    }

    public void setAttacktree_node(attacktree_Node attacktree_node) {
        this.attacktree_node = attacktree_node;
    }

}