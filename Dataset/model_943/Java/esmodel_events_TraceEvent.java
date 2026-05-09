





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_TraceEvent extends Event {

    private String featureName;



    public esmodel_events_TraceEvent(
        String featureName    ) {
        super(
        );
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}