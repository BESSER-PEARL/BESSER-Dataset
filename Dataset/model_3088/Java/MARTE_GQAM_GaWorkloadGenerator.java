





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaWorkloadGenerator  {

    private String pop;





    private GQAM_MARTE_Behavior gqam_marte_behavior;


    public MARTE_GQAM_GaWorkloadGenerator(
        String pop    ) {
        this.pop = pop;
    }


    public String getPop() {
        return pop;
    }

    public void setPop(String pop) {
        this.pop = pop;
    }

    public GQAM_MARTE_Behavior getGqam_marte_behavior() {
        return gqam_marte_behavior;
    }

    public void setGqam_marte_behavior(GQAM_MARTE_Behavior gqam_marte_behavior) {
        this.gqam_marte_behavior = gqam_marte_behavior;
    }

}