





import java.util.List;
import java.util.ArrayList;

public class attacktree_Node  {

    private String tags;
    private String name;
    private String domains;
    private String description;





    private attacktree_Node attacktree_node;


    public attacktree_Node(
        String tags,        String name,        String domains,        String description    ) {
        this.tags = tags;
        this.name = name;
        this.domains = domains;
        this.description = description;
    }


    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDomains() {
        return domains;
    }

    public void setDomains(String domains) {
        this.domains = domains;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public attacktree_Node getAttacktree_node() {
        return attacktree_node;
    }

    public void setAttacktree_node(attacktree_Node attacktree_node) {
        this.attacktree_node = attacktree_node;
    }

}