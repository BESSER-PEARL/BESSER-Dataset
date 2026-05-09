





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_ScheduledTime extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float startTime;
    private float duration;
    private boolean restart;
    private int cycle;



    public oaam_allocations_ScheduledTime(
        float startTime,        float duration,        boolean restart,        int cycle    ) {
        super(
        );
        this.startTime = startTime;
        this.duration = duration;
        this.restart = restart;
        this.cycle = cycle;
    }


    public float getStarttime() {
        return startTime;
    }

    public void setStarttime(float startTime) {
        this.startTime = startTime;
    }
    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }
    public boolean getRestart() {
        return restart;
    }

    public void setRestart(boolean restart) {
        this.restart = restart;
    }
    public int getCycle() {
        return cycle;
    }

    public void setCycle(int cycle) {
        this.cycle = cycle;
    }


}