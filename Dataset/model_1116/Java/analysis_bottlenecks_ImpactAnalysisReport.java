





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_ImpactAnalysisReport extends AnalysisReport {

    private boolean classLevel;



    public analysis_bottlenecks_ImpactAnalysisReport(
        boolean classLevel    ) {
        super(
        );
        this.classLevel = classLevel;
    }


    public boolean getClasslevel() {
        return classLevel;
    }

    public void setClasslevel(boolean classLevel) {
        this.classLevel = classLevel;
    }


}