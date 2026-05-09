





import java.util.List;
import java.util.ArrayList;

public class oclstates_Event  {

    private String name;





    private oclstates_Statemachine oclstates_statemachine;


    public oclstates_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public oclstates_Statemachine getOclstates_statemachine() {
        return oclstates_statemachine;
    }

    public void setOclstates_statemachine(oclstates_Statemachine oclstates_statemachine) {
        this.oclstates_statemachine = oclstates_statemachine;
    }

}