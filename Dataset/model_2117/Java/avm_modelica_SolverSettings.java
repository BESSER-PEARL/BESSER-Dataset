





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_SolverSettings extends Settings {

    private String StopTime;
    private String IntervalMethod;
    private String NumberOfIntervals;
    private String JobManagerToolSelection;
    private String ToolSpecificAnnotations;
    private String Solver;
    private String StartTime;
    private String Tolerance;
    private String IntervalLength;



    public avm_modelica_SolverSettings(
        String StopTime,        String IntervalMethod,        String NumberOfIntervals,        String JobManagerToolSelection,        String ToolSpecificAnnotations,        String Solver,        String StartTime,        String Tolerance,        String IntervalLength    ) {
        super(
        );
        this.StopTime = StopTime;
        this.IntervalMethod = IntervalMethod;
        this.NumberOfIntervals = NumberOfIntervals;
        this.JobManagerToolSelection = JobManagerToolSelection;
        this.ToolSpecificAnnotations = ToolSpecificAnnotations;
        this.Solver = Solver;
        this.StartTime = StartTime;
        this.Tolerance = Tolerance;
        this.IntervalLength = IntervalLength;
    }


    public String getStoptime() {
        return StopTime;
    }

    public void setStoptime(String StopTime) {
        this.StopTime = StopTime;
    }
    public String getIntervalmethod() {
        return IntervalMethod;
    }

    public void setIntervalmethod(String IntervalMethod) {
        this.IntervalMethod = IntervalMethod;
    }
    public String getNumberofintervals() {
        return NumberOfIntervals;
    }

    public void setNumberofintervals(String NumberOfIntervals) {
        this.NumberOfIntervals = NumberOfIntervals;
    }
    public String getJobmanagertoolselection() {
        return JobManagerToolSelection;
    }

    public void setJobmanagertoolselection(String JobManagerToolSelection) {
        this.JobManagerToolSelection = JobManagerToolSelection;
    }
    public String getToolspecificannotations() {
        return ToolSpecificAnnotations;
    }

    public void setToolspecificannotations(String ToolSpecificAnnotations) {
        this.ToolSpecificAnnotations = ToolSpecificAnnotations;
    }
    public String getSolver() {
        return Solver;
    }

    public void setSolver(String Solver) {
        this.Solver = Solver;
    }
    public String getStarttime() {
        return StartTime;
    }

    public void setStarttime(String StartTime) {
        this.StartTime = StartTime;
    }
    public String getTolerance() {
        return Tolerance;
    }

    public void setTolerance(String Tolerance) {
        this.Tolerance = Tolerance;
    }
    public String getIntervallength() {
        return IntervalLength;
    }

    public void setIntervallength(String IntervalLength) {
        this.IntervalLength = IntervalLength;
    }


}