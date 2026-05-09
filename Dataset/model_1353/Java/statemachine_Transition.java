





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition extends ObeoDSMObject {

    private String guard;



    public statemachine_Transition(
        String guard    ) {
        super(
        );
        this.guard = guard;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }


}