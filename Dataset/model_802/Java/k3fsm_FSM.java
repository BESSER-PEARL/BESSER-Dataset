





import java.util.List;
import java.util.ArrayList;

public class k3fsm_FSM  {

    private String name;
    private String consummedString;
    private String unprocessedString;
    private String producedString;



    public k3fsm_FSM(
        String name,        String consummedString,        String unprocessedString,        String producedString    ) {
        this.name = name;
        this.consummedString = consummedString;
        this.unprocessedString = unprocessedString;
        this.producedString = producedString;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }
    public String getUnprocessedstring() {
        return unprocessedString;
    }

    public void setUnprocessedstring(String unprocessedString) {
        this.unprocessedString = unprocessedString;
    }
    public String getProducedstring() {
        return producedString;
    }

    public void setProducedstring(String producedString) {
        this.producedString = producedString;
    }


}