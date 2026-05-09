





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_Schedule extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private int priority;
    private float rate;
    private boolean isPeriodic;



    public oaam_allocations_Schedule(
        int priority,        float rate,        boolean isPeriodic    ) {
        super(
        );
        this.priority = priority;
        this.rate = rate;
        this.isPeriodic = isPeriodic;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public float getRate() {
        return rate;
    }

    public void setRate(float rate) {
        this.rate = rate;
    }
    public boolean getIsperiodic() {
        return isPeriodic;
    }

    public void setIsperiodic(boolean isPeriodic) {
        this.isPeriodic = isPeriodic;
    }


}