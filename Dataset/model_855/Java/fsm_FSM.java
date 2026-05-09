





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {

    private String consummedString;
    private String underProcessTrigger;
    private String name;



    public fsm_FSM(
        String consummedString,        String underProcessTrigger,        String name    ) {
        this.consummedString = consummedString;
        this.underProcessTrigger = underProcessTrigger;
        this.name = name;
    }


    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }
    public String getUnderprocesstrigger() {
        return underProcessTrigger;
    }

    public void setUnderprocesstrigger(String underProcessTrigger) {
        this.underProcessTrigger = underProcessTrigger;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}