





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_SolverSettings extends Settings {

    private String IntervalMethod;
    private String StopTime;
    private String ToolSpecificAnnotations;
    private String JobManagerToolSelection;
    private String Tolerance;
    private String StartTime;
    private String Solver;
    private String IntervalLength;
    private String NumberOfIntervals;



    public avm_modelica_SolverSettings(
        String IntervalMethod,        String StopTime,        String ToolSpecificAnnotations,        String JobManagerToolSelection,        String Tolerance,        String StartTime,        String Solver,        String IntervalLength,        String NumberOfIntervals    ) {
        super(
        );
        this.IntervalMethod = IntervalMethod;
        this.StopTime = StopTime;
        this.ToolSpecificAnnotations = ToolSpecificAnnotations;
        this.JobManagerToolSelection = JobManagerToolSelection;
        this.Tolerance = Tolerance;
        this.StartTime = StartTime;
        this.Solver = Solver;
        this.IntervalLength = IntervalLength;
        this.NumberOfIntervals = NumberOfIntervals;
    }


    public String getIntervalmethod() {
        return IntervalMethod;
    }

    public void setIntervalmethod(String IntervalMethod) {
        this.IntervalMethod = IntervalMethod;
    }
    public String getStoptime() {
        return StopTime;
    }

    public void setStoptime(String StopTime) {
        this.StopTime = StopTime;
    }
    public String getToolspecificannotations() {
        return ToolSpecificAnnotations;
    }

    public void setToolspecificannotations(String ToolSpecificAnnotations) {
        this.ToolSpecificAnnotations = ToolSpecificAnnotations;
    }
    public String getJobmanagertoolselection() {
        return JobManagerToolSelection;
    }

    public void setJobmanagertoolselection(String JobManagerToolSelection) {
        this.JobManagerToolSelection = JobManagerToolSelection;
    }
    public String getTolerance() {
        return Tolerance;
    }

    public void setTolerance(String Tolerance) {
        this.Tolerance = Tolerance;
    }
    public String getStarttime() {
        return StartTime;
    }

    public void setStarttime(String StartTime) {
        this.StartTime = StartTime;
    }
    public String getSolver() {
        return Solver;
    }

    public void setSolver(String Solver) {
        this.Solver = Solver;
    }
    public String getIntervallength() {
        return IntervalLength;
    }

    public void setIntervallength(String IntervalLength) {
        this.IntervalLength = IntervalLength;
    }
    public String getNumberofintervals() {
        return NumberOfIntervals;
    }

    public void setNumberofintervals(String NumberOfIntervals) {
        this.NumberOfIntervals = NumberOfIntervals;
    }


}