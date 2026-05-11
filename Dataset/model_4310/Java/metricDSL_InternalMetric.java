





import java.util.List;
import java.util.ArrayList;

public class metricDSL_InternalMetric extends Metric {

    private String shortName;
    private String description;



    public metricDSL_InternalMetric(
        String shortName,        String description    ) {
        super(
        );
        this.shortName = shortName;
        this.description = description;
    }


    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}