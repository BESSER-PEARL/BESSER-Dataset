





import java.util.List;
import java.util.ArrayList;

public class dsl_PersistentEffect extends Effect {

    private String ranges;
    private int periodCount;
    private String durations;





    private List<dsl_Effect> dsl_effects;


    public dsl_PersistentEffect(
        String ranges,        int periodCount,        String durations    ) {
        super(
        );
        this.ranges = ranges;
        this.periodCount = periodCount;
        this.durations = durations;
        this.dsl_effects = new ArrayList<>();
    }

    public dsl_PersistentEffect(
        String ranges,        int periodCount,        String durations        ArrayList<dsl_Effect> dsl_effects    ) {
        this.ranges = ranges;
        this.periodCount = periodCount;
        this.durations = durations;
        this.dsl_effects = dsl_effects;
    }

    public String getRanges() {
        return ranges;
    }

    public void setRanges(String ranges) {
        this.ranges = ranges;
    }
    public int getPeriodcount() {
        return periodCount;
    }

    public void setPeriodcount(int periodCount) {
        this.periodCount = periodCount;
    }
    public String getDurations() {
        return durations;
    }

    public void setDurations(String durations) {
        this.durations = durations;
    }

    public List<dsl_Effect> getDsl_effects() {
        return dsl_effects;
    }

    public void addDsl_effect(Dsl_effect dsl_effect) {
        this.dsl_effects.add(dsl_effect);
    }

}