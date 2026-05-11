





import java.util.List;
import java.util.ArrayList;

public class operators_Node extends Base {

    private String nodeID;





    private operators_ResourceExpansion operators_resourceexpansion;




    private operators_Relationship operators_relationship;




    private operators_Relationship operators_relationship;


    public operators_Node(
        String nodeID    ) {
        super(
        );
        this.nodeID = nodeID;
    }


    public String getNodeid() {
        return nodeID;
    }

    public void setNodeid(String nodeID) {
        this.nodeID = nodeID;
    }

    public operators_ResourceExpansion getOperators_resourceexpansion() {
        return operators_resourceexpansion;
    }

    public void setOperators_resourceexpansion(operators_ResourceExpansion operators_resourceexpansion) {
        this.operators_resourceexpansion = operators_resourceexpansion;
    }
    public operators_Relationship getOperators_relationship() {
        return operators_relationship;
    }

    public void setOperators_relationship(operators_Relationship operators_relationship) {
        this.operators_relationship = operators_relationship;
    }
    public operators_Relationship getOperators_relationship() {
        return operators_relationship;
    }

    public void setOperators_relationship(operators_Relationship operators_relationship) {
        this.operators_relationship = operators_relationship;
    }

}