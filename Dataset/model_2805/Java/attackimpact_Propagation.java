





import java.util.List;
import java.util.ArrayList;

public class attackimpact_Propagation  {

    private int severity;
    private String tags;
    private String type;





    private attackimpact_Node attackimpact_node;




    private List<attackimpact_Node> attackimpact_nodes;




    private attackimpact_Vulnerability attackimpact_vulnerability;


    public attackimpact_Propagation(
        int severity,        String tags,        String type    ) {
        this.severity = severity;
        this.tags = tags;
        this.type = type;
        this.attackimpact_nodes = new ArrayList<>();
    }

    public attackimpact_Propagation(
        int severity,        String tags,        String type        ArrayList<attackimpact_Node> attackimpact_nodes    ) {
        this.severity = severity;
        this.tags = tags;
        this.type = type;
        this.attackimpact_nodes = attackimpact_nodes;
    }

    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }
    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public attackimpact_Node getAttackimpact_node() {
        return attackimpact_node;
    }

    public void setAttackimpact_node(attackimpact_Node attackimpact_node) {
        this.attackimpact_node = attackimpact_node;
    }
    public List<attackimpact_Node> getAttackimpact_nodes() {
        return attackimpact_nodes;
    }

    public void addAttackimpact_node(Attackimpact_node attackimpact_node) {
        this.attackimpact_nodes.add(attackimpact_node);
    }
    public attackimpact_Vulnerability getAttackimpact_vulnerability() {
        return attackimpact_vulnerability;
    }

    public void setAttackimpact_vulnerability(attackimpact_Vulnerability attackimpact_vulnerability) {
        this.attackimpact_vulnerability = attackimpact_vulnerability;
    }

}