





import java.util.List;
import java.util.ArrayList;

public class fault_tree_BasicEvent extends Event {

    private float probability;





    private List<fault_tree_ErrorInstance> fault_tree_errorinstances;




    private fault_tree_ErrorInstance fault_tree_errorinstance;


    public fault_tree_BasicEvent(
        float probability    ) {
        super(
        );
        this.probability = probability;
        this.fault_tree_errorinstances = new ArrayList<>();
    }

    public fault_tree_BasicEvent(
        float probability        ArrayList<fault_tree_ErrorInstance> fault_tree_errorinstances    ) {
        this.probability = probability;
        this.fault_tree_errorinstances = fault_tree_errorinstances;
    }

    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }

    public List<fault_tree_ErrorInstance> getFault_tree_errorinstances() {
        return fault_tree_errorinstances;
    }

    public void addFault_tree_errorinstance(Fault_tree_errorinstance fault_tree_errorinstance) {
        this.fault_tree_errorinstances.add(fault_tree_errorinstance);
    }
    public fault_tree_ErrorInstance getFault_tree_errorinstance() {
        return fault_tree_errorinstance;
    }

    public void setFault_tree_errorinstance(fault_tree_ErrorInstance fault_tree_errorinstance) {
        this.fault_tree_errorinstance = fault_tree_errorinstance;
    }

}