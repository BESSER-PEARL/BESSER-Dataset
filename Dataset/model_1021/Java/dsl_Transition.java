





import java.util.List;
import java.util.ArrayList;

public class dsl_Transition  {

    private String name;
    private String trigger;



    public dsl_Transition(
        String name,        String trigger    ) {
        this.name = name;
        this.trigger = trigger;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }


}