





import java.util.List;
import java.util.ArrayList;

public class guigraph_Transition extends rules_IRealTimeConsumer, GuiGraphNode {

    private String timeMax;
    private String timingType;
    private float risk;
    private boolean terminates;
    private String timeMin;



    public guigraph_Transition(
        String timeMax,        String timingType,        float risk,        boolean terminates,        String timeMin    ) {
        super(
        );
        this.timeMax = timeMax;
        this.timingType = timingType;
        this.risk = risk;
        this.terminates = terminates;
        this.timeMin = timeMin;
    }


    public String getTimemax() {
        return timeMax;
    }

    public void setTimemax(String timeMax) {
        this.timeMax = timeMax;
    }
    public String getTimingtype() {
        return timingType;
    }

    public void setTimingtype(String timingType) {
        this.timingType = timingType;
    }
    public float getRisk() {
        return risk;
    }

    public void setRisk(float risk) {
        this.risk = risk;
    }
    public boolean getTerminates() {
        return terminates;
    }

    public void setTerminates(boolean terminates) {
        this.terminates = terminates;
    }
    public String getTimemin() {
        return timeMin;
    }

    public void setTimemin(String timeMin) {
        this.timeMin = timeMin;
    }


}