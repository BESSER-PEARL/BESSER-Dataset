





import java.util.List;
import java.util.ArrayList;

public class avm_cad_CoordinateSystem extends Datum {






    private List<Metric> metrics;


    public avm_cad_CoordinateSystem(
    ) {
        super(
        );
        this.metrics = new ArrayList<>();
    }

    public avm_cad_CoordinateSystem(
        ArrayList<Metric> metrics    ) {
        this.metrics = metrics;
    }


    public List<Metric> getMetrics() {
        return metrics;
    }

    public void addMetric(Metric metric) {
        this.metrics.add(metric);
    }

}