





import java.util.List;
import java.util.ArrayList;

public class faultTree_ConditioningEvent extends Event {

    private String condition;





    private faultTree_FaultTree faulttree_faulttree;


    public faultTree_ConditioningEvent(
        String condition    ) {
        super(
        );
        this.condition = condition;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public faultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(faultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }

}