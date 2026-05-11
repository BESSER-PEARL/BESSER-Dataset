





import java.util.List;
import java.util.ArrayList;

public class faultTree_PrimaryEvent extends Event {

    private float probability;
    private String type;





    private faultTree_FaultTree faulttree_faulttree;


    public faultTree_PrimaryEvent(
        float probability,        String type    ) {
        super(
        );
        this.probability = probability;
        this.type = type;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public faultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(faultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }

}