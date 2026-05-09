





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String producedString;
    private String unprocessedString;
    private String consummedString;



    public fsm_StateMachine(
        String producedString,        String unprocessedString,        String consummedString    ) {
        super(
        );
        this.producedString = producedString;
        this.unprocessedString = unprocessedString;
        this.consummedString = consummedString;
    }


    public String getProducedstring() {
        return producedString;
    }

    public void setProducedstring(String producedString) {
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


}