





import java.util.List;
import java.util.ArrayList;

public class statesml_Event  {

    private String name;





    private statesml_Trigger statesml_trigger;


    public statesml_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_Trigger getStatesml_trigger() {
        return statesml_trigger;
    }

    public void setStatesml_trigger(statesml_Trigger statesml_trigger) {
        this.statesml_trigger = statesml_trigger;
    }

}