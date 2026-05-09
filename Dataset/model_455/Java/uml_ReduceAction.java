





import java.util.List;
import java.util.ArrayList;

public class uml_ReduceAction extends Action {

    private String isOrdered;





    private uml_Behavior uml_behavior;


    public uml_ReduceAction(
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

    public uml_Behavior getUml_behavior() {
        return uml_behavior;
    }

    public void setUml_behavior(uml_Behavior uml_behavior) {
        this.uml_behavior = uml_behavior;
    }

}