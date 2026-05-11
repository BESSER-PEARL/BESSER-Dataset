





import java.util.List;
import java.util.ArrayList;

public class avm_cad_Datum extends DomainModelPort {

    private String DatumName;





    private List<Metric> metrics;


    public avm_cad_Datum(
        String DatumName    ) {
        super(
        );
        this.DatumName = DatumName;
        this.metrics = new ArrayList<>();
    }

    public avm_cad_Datum(
        String DatumName        ArrayList<Metric> metrics    ) {
        this.DatumName = DatumName;
        this.metrics = metrics;
    }

    public String getDatumname() {
        return DatumName;
    }

    public void setDatumname(String DatumName) {
        this.DatumName = DatumName;
    }

    public List<Metric> getMetrics() {
        return metrics;
    }

    public void addMetric(Metric metric) {
        this.metrics.add(metric);
    }

}