





import java.util.List;
import java.util.ArrayList;

public class analysis_postprocessing_PostProcessingReport extends AnalysisReport {

    private boolean deadlock;
    private float time;



    public analysis_postprocessing_PostProcessingReport(
        boolean deadlock,        float time    ) {
        super(
        );
        this.deadlock = deadlock;
        this.time = time;
    }


    public boolean getDeadlock() {
        return deadlock;
    }

    public void setDeadlock(boolean deadlock) {
        this.deadlock = deadlock;
    }
    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }


}