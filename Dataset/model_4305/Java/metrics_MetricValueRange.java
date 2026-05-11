





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricValueRange  {

    private String kindHint;
    private String intervalHint;



    public metrics_MetricValueRange(
        String kindHint,        String intervalHint    ) {
        this.kindHint = kindHint;
        this.intervalHint = intervalHint;
    }


    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }
    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }


}