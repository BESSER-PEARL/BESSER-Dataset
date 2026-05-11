





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_TimingConstraint  {

    private String minmax;
    private String timingConstraint;





    private reqLanguage_Time reqlanguage_time;




    private reqLanguage_PrefixCondition reqlanguage_prefixcondition;


    public reqLanguage_TimingConstraint(
        String minmax,        String timingConstraint    ) {
        this.minmax = minmax;
        this.timingConstraint = timingConstraint;
    }


    public String getMinmax() {
        return minmax;
    }

    public void setMinmax(String minmax) {
        this.minmax = minmax;
    }
    public String getTimingconstraint() {
        return timingConstraint;
    }

    public void setTimingconstraint(String timingConstraint) {
        this.timingConstraint = timingConstraint;
    }

    public reqLanguage_Time getReqlanguage_time() {
        return reqlanguage_time;
    }

    public void setReqlanguage_time(reqLanguage_Time reqlanguage_time) {
        this.reqlanguage_time = reqlanguage_time;
    }
    public reqLanguage_PrefixCondition getReqlanguage_prefixcondition() {
        return reqlanguage_prefixcondition;
    }

    public void setReqlanguage_prefixcondition(reqLanguage_PrefixCondition reqlanguage_prefixcondition) {
        this.reqlanguage_prefixcondition = reqlanguage_prefixcondition;
    }

}