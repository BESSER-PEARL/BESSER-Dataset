





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {

    private String consummedString;
    private String name;
    private String underProcessTrigger;



    public fsm_FSM(
        String consummedString,        String name,        String underProcessTrigger    ) {
        this.consummedString = consummedString;
        this.name = name;
        this.underProcessTrigger = underProcessTrigger;
    }


    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnderprocesstrigger() {
        return underProcessTrigger;
    }

    public void setUnderprocesstrigger(String underProcessTrigger) {
        this.underProcessTrigger = underProcessTrigger;
    }


}