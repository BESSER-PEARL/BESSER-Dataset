





import java.util.List;
import java.util.ArrayList;

public class dtmc_Module  {

    private boolean isAutonomous;





    private dtmc_Dtmc dtmc_dtmc;




    private dtmc_Node dtmc_node;




    private List<dtmc_Node> dtmc_nodes;


    public dtmc_Module(
        boolean isAutonomous    ) {
        this.isAutonomous = isAutonomous;
        this.dtmc_nodes = new ArrayList<>();
    }

    public dtmc_Module(
        boolean isAutonomous        ArrayList<dtmc_Node> dtmc_nodes    ) {
        this.isAutonomous = isAutonomous;
        this.dtmc_nodes = dtmc_nodes;
    }

    public boolean getIsautonomous() {
        return isAutonomous;
    }

    public void setIsautonomous(boolean isAutonomous) {
        this.isAutonomous = isAutonomous;
    }

    public dtmc_Dtmc getDtmc_dtmc() {
        return dtmc_dtmc;
    }

    public void setDtmc_dtmc(dtmc_Dtmc dtmc_dtmc) {
        this.dtmc_dtmc = dtmc_dtmc;
    }
    public dtmc_Node getDtmc_node() {
        return dtmc_node;
    }

    public void setDtmc_node(dtmc_Node dtmc_node) {
        this.dtmc_node = dtmc_node;
    }
    public List<dtmc_Node> getDtmc_nodes() {
        return dtmc_nodes;
    }

    public void addDtmc_node(Dtmc_node dtmc_node) {
        this.dtmc_nodes.add(dtmc_node);
    }

}