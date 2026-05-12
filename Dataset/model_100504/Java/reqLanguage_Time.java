





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Time  {

    private String timeUnit;
    private int value;





    private reqLanguage_TimingConstraint reqlanguage_timingconstraint;


    public reqLanguage_Time(
        String timeUnit,        int value    ) {
        this.timeUnit = timeUnit;
        this.value = value;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public reqLanguage_TimingConstraint getReqlanguage_timingconstraint() {
        return reqlanguage_timingconstraint;
    }

    public void setReqlanguage_timingconstraint(reqLanguage_TimingConstraint reqlanguage_timingconstraint) {
        this.reqlanguage_timingconstraint = reqlanguage_timingconstraint;
    }

}