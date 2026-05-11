





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricValueRange  {

    private String kindHint;
    private String periodHint;



    public metrics_MetricValueRange(
        String kindHint,        String periodHint    ) {
        this.kindHint = kindHint;
        this.periodHint = periodHint;
    }


    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }
    public String getPeriodhint() {
        return periodHint;
    }

    public void setPeriodhint(String periodHint) {
        this.periodHint = periodHint;
    }


}