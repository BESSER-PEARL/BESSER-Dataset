





import java.util.List;
import java.util.ArrayList;

public class wsn_Cluster  {






    private wsn_ClusterHead wsn_clusterhead;




    private List<wsn_Node> wsn_nodes;


    public wsn_Cluster(
    ) {
        this.wsn_nodes = new ArrayList<>();
    }

    public wsn_Cluster(
        ArrayList<wsn_Node> wsn_nodes    ) {
        this.wsn_nodes = wsn_nodes;
    }


    public wsn_ClusterHead getWsn_clusterhead() {
        return wsn_clusterhead;
    }

    public void setWsn_clusterhead(wsn_ClusterHead wsn_clusterhead) {
        this.wsn_clusterhead = wsn_clusterhead;
    }
    public List<wsn_Node> getWsn_nodes() {
        return wsn_nodes;
    }

    public void addWsn_node(Wsn_node wsn_node) {
        this.wsn_nodes.add(wsn_node);
    }

}