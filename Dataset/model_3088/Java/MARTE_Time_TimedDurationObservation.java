





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_TimedDurationObservation extends TimedElement {

    private String obsKind;



    public MARTE_Time_TimedDurationObservation(
        String obsKind    ) {
        super(
        );
        this.obsKind = obsKind;
    }


    public String getObskind() {
        return obsKind;
    }

    public void setObskind(String obsKind) {
        this.obsKind = obsKind;
    }


}