





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_TimerResource extends TimingResource {

    private String duration;
    private String isPeriodic;



    public MARTE_GRM_TimerResource(
        String duration,        String isPeriodic    ) {
        super(
        );
        this.duration = duration;
        this.isPeriodic = isPeriodic;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getIsperiodic() {
        return isPeriodic;
    }

    public void setIsperiodic(String isPeriodic) {
        this.isPeriodic = isPeriodic;
    }


}