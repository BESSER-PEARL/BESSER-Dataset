





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ReduceAction extends Action {

    private String isOrdered;





    private uml3_0_0_Behavior uml3_0_0_behavior;


    public uml3_0_0_ReduceAction(
        String isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }

    public uml3_0_0_Behavior getUml3_0_0_behavior() {
        return uml3_0_0_behavior;
    }

    public void setUml3_0_0_behavior(uml3_0_0_Behavior uml3_0_0_behavior) {
        this.uml3_0_0_behavior = uml3_0_0_behavior;
    }

}