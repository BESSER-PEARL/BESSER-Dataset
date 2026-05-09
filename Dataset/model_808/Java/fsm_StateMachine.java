





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String unprocessedString;
    private String consummedString;
    private String producedString;



    public fsm_StateMachine(
        String unprocessedString,        String consummedString,        String producedString    ) {
        super(
        );
        this.unprocessedString = unprocessedString;
        this.consummedString = consummedString;
        this.producedString = producedString;
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