





import java.util.List;
import java.util.ArrayList;

public class operators_Node extends Base {

    private String nodeID;





    private operators_Warehouse operators_warehouse;




    private operators_Relationship operators_relationship;




    private operators_Network operators_network;




    private operators_Relationship operators_relationship;




    private operators_ResourceExpansion operators_resourceexpansion;




    private operators_ResourceMonitor operators_resourcemonitor;


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

    public operators_Warehouse getOperators_warehouse() {
        return operators_warehouse;
    }

    public void setOperators_warehouse(operators_Warehouse operators_warehouse) {
        this.operators_warehouse = operators_warehouse;
    }
    public operators_Relationship getOperators_relationship() {
        return operators_relationship;
    }

    public void setOperators_relationship(operators_Relationship operators_relationship) {
        this.operators_relationship = operators_relationship;
    }
    public operators_Network getOperators_network() {
        return operators_network;
    }

    public void setOperators_network(operators_Network operators_network) {
        this.operators_network = operators_network;
    }
    public operators_Relationship getOperators_relationship() {
        return operators_relationship;
    }

    public void setOperators_relationship(operators_Relationship operators_relationship) {
        this.operators_relationship = operators_relationship;
    }
    public operators_ResourceExpansion getOperators_resourceexpansion() {
        return operators_resourceexpansion;
    }

    public void setOperators_resourceexpansion(operators_ResourceExpansion operators_resourceexpansion) {
        this.operators_resourceexpansion = operators_resourceexpansion;
    }
    public operators_ResourceMonitor getOperators_resourcemonitor() {
        return operators_resourcemonitor;
    }

    public void setOperators_resourcemonitor(operators_ResourceMonitor operators_resourcemonitor) {
        this.operators_resourcemonitor = operators_resourcemonitor;
    }

}