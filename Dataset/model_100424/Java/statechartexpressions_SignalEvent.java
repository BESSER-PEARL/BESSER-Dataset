





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_SignalEvent extends Event {

    private String identifier;



    public statechartexpressions_SignalEvent(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}