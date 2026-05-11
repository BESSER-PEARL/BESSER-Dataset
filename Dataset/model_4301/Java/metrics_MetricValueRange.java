





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricValueRange  {

    private String intervalHint;
    private String kindHint;



    public metrics_MetricValueRange(
        String intervalHint,        String kindHint    ) {
        this.intervalHint = intervalHint;
        this.kindHint = kindHint;
    }


    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }
    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }


}