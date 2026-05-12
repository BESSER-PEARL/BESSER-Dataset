





import java.util.List;
import java.util.ArrayList;

public class State_Machines_SynchState extends StateVertex {

    private String bound;



    public State_Machines_SynchState(
        String bound    ) {
        super(
        );
        this.bound = bound;
    }


    public String getBound() {
        return bound;
    }

    public void setBound(String bound) {
        this.bound = bound;
    }


}