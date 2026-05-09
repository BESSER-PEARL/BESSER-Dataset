





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_DPbase_Link  {

    private String cp_name;
    private int maxNodes;
    private int speed;



    public MachineLibrary_DPbase_Link(
        String cp_name,        int maxNodes,        int speed    ) {
        this.cp_name = cp_name;
        this.maxNodes = maxNodes;
        this.speed = speed;
    }


    public String getCp_name() {
        return cp_name;
    }

    public void setCp_name(String cp_name) {
        this.cp_name = cp_name;
    }
    public int getMaxnodes() {
        return maxNodes;
    }

    public void setMaxnodes(int maxNodes) {
        this.maxNodes = maxNodes;
    }
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }


}