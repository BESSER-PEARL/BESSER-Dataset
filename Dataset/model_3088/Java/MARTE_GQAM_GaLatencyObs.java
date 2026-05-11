





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaLatencyObs extends GaTimedObs {

    private String miss;
    private String maxJitter;
    private String utility;
    private String latency;



    public MARTE_GQAM_GaLatencyObs(
        String miss,        String maxJitter,        String utility,        String latency    ) {
        super(
        );
        this.miss = miss;
        this.maxJitter = maxJitter;
        this.utility = utility;
        this.latency = latency;
    }


    public String getMiss() {
        return miss;
    }

    public void setMiss(String miss) {
        this.miss = miss;
    }
    public String getMaxjitter() {
        return maxJitter;
    }

    public void setMaxjitter(String maxJitter) {
        this.maxJitter = maxJitter;
    }
    public String getUtility() {
        return utility;
    }

    public void setUtility(String utility) {
        this.utility = utility;
    }
    public String getLatency() {
        return latency;
    }

    public void setLatency(String latency) {
        this.latency = latency;
    }


}