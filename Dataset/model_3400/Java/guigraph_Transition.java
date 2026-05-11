





import java.util.List;
import java.util.ArrayList;

public class guigraph_Transition extends GuiGraphNode, rules_IRealTimeConsumer {

    private int rate;
    private String timingType;
    private float faultProbability;
    private String timeMax;
    private boolean terminates;
    private String timeMin;
    private float faultImpact;



    public guigraph_Transition(
        int rate,        String timingType,        float faultProbability,        String timeMax,        boolean terminates,        String timeMin,        float faultImpact    ) {
        super(
        );
        this.rate = rate;
        this.timingType = timingType;
        this.faultProbability = faultProbability;
        this.timeMax = timeMax;
        this.terminates = terminates;
        this.timeMin = timeMin;
        this.faultImpact = faultImpact;
    }


    public int getRate() {
        return rate;
    }

    public void setRate(int rate) {
        this.rate = rate;
    }
    public String getTimingtype() {
        return timingType;
    }

    public void setTimingtype(String timingType) {
        this.timingType = timingType;
    }
    public float getFaultprobability() {
        return faultProbability;
    }

    public void setFaultprobability(float faultProbability) {
        this.faultProbability = faultProbability;
    }
    public String getTimemax() {
        return timeMax;
    }

    public void setTimemax(String timeMax) {
        this.timeMax = timeMax;
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
    public float getFaultimpact() {
        return faultImpact;
    }

    public void setFaultimpact(float faultImpact) {
        this.faultImpact = faultImpact;
    }


}