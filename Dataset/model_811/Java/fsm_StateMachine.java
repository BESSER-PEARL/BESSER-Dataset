





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String unprocessedString;
    private String producedString;
    private String consummedString;



    public fsm_StateMachine(
        String unprocessedString,        String producedString,        String consummedString    ) {
        super(
        );
        this.unprocessedString = unprocessedString;
        this.producedString = producedString;
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
    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }


}