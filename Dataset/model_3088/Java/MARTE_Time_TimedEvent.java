





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_TimedEvent extends TimedElement {

    private String repetition;



    public MARTE_Time_TimedEvent(
        String repetition    ) {
        super(
        );
        this.repetition = repetition;
    }


    public String getRepetition() {
        return repetition;
    }

    public void setRepetition(String repetition) {
        this.repetition = repetition;
    }


}