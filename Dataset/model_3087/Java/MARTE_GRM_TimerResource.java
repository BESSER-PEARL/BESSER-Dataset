





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_TimerResource extends TimingResource {

    private String isPeriodic;



    public MARTE_GRM_TimerResource(
        String isPeriodic    ) {
        super(
        );
        this.isPeriodic = isPeriodic;
    }


    public String getIsperiodic() {
        return isPeriodic;
    }

    public void setIsperiodic(String isPeriodic) {
        this.isPeriodic = isPeriodic;
    }


}