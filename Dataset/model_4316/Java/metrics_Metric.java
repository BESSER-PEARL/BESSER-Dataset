





import java.util.List;
import java.util.ArrayList;

public class metrics_Metric extends Base {

    private String name;





    private metrics_Addon metrics_addon;


    public metrics_Metric(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metrics_Addon getMetrics_addon() {
        return metrics_addon;
    }

    public void setMetrics_addon(metrics_Addon metrics_addon) {
        this.metrics_addon = metrics_addon;
    }

}