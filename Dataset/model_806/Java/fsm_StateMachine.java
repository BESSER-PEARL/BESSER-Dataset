





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String consummedString;
    private String unprocessedString;
    private String producedString;



    public fsm_StateMachine(
        String consummedString,        String unprocessedString,        String producedString    ) {
        super(
        );
        this.consummedString = consummedString;
        this.unprocessedString = unprocessedString;
        this.producedString = producedString;
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