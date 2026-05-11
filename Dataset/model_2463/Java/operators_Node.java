





import java.util.List;
import java.util.ArrayList;

public class operators_Node  {

    private String nodeID;





    private operators_Network operators_network;


    public operators_Node(
        String nodeID    ) {
        this.nodeID = nodeID;
    }


    public String getNodeid() {
        return nodeID;
    }

    public void setNodeid(String nodeID) {
        this.nodeID = nodeID;
    }

    public operators_Network getOperators_network() {
        return operators_network;
    }

    public void setOperators_network(operators_Network operators_network) {
        this.operators_network = operators_network;
    }

}