





import java.util.List;
import java.util.ArrayList;

public class wsn_Network  {






    private wsn_Objectives wsn_objectives;




    private List<wsn_Node> wsn_nodes;


    public wsn_Network(
    ) {
        this.wsn_nodes = new ArrayList<>();
    }

    public wsn_Network(
        ArrayList<wsn_Node> wsn_nodes    ) {
        this.wsn_nodes = wsn_nodes;
    }


    public wsn_Objectives getWsn_objectives() {
        return wsn_objectives;
    }

    public void setWsn_objectives(wsn_Objectives wsn_objectives) {
        this.wsn_objectives = wsn_objectives;
    }
    public List<wsn_Node> getWsn_nodes() {
        return wsn_nodes;
    }

    public void addWsn_node(Wsn_node wsn_node) {
        this.wsn_nodes.add(wsn_node);
    }

}