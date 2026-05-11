





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_TimedInstantObservation extends TimedObservation {

    private String obsKind;





    private Time_MARTE_TimeObservation time_marte_timeobservation;


    public MARTE_Time_TimedInstantObservation(
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

    public Time_MARTE_TimeObservation getTime_marte_timeobservation() {
        return time_marte_timeobservation;
    }

    public void setTime_marte_timeobservation(Time_MARTE_TimeObservation time_marte_timeobservation) {
        this.time_marte_timeobservation = time_marte_timeobservation;
    }

}