





import java.util.List;
import java.util.ArrayList;

public class fsm_FiniteStateMachine  {

    private String name;
    private String unprocessedString;
    private String consummedString;
    private String producedString;



    public fsm_FiniteStateMachine(
        String name,        String unprocessedString,        String consummedString,        String producedString    ) {
        this.name = name;
        this.unprocessedString = unprocessedString;
        this.consummedString = consummedString;
        this.producedString = producedString;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnprocessedstring() {
        return unprocessedString;
    }

    public void setUnprocessedstring(String unprocessedString) {
        this.unprocessedString = unprocessedString;
    }
    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }
    public String getProducedstring() {
        return producedString;
    }

    public void setProducedstring(String producedString) {
        this.producedString = producedString;
    }


}