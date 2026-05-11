





import java.util.List;
import java.util.ArrayList;

public class transport_PipeTransportEdgeLabelValue extends LabelValue {

    private float maxFlow;
    private String timePeriod;



    public transport_PipeTransportEdgeLabelValue(
        float maxFlow,        String timePeriod    ) {
        super(
        );
        this.maxFlow = maxFlow;
        this.timePeriod = timePeriod;
    }


    public float getMaxflow() {
        return maxFlow;
    }

    public void setMaxflow(float maxFlow) {
        this.maxFlow = maxFlow;
    }
    public String getTimeperiod() {
        return timePeriod;
    }

    public void setTimeperiod(String timePeriod) {
        this.timePeriod = timePeriod;
    }


}