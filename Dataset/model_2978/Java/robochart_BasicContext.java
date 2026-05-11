





import java.util.List;
import java.util.ArrayList;

public class robochart_BasicContext  {






    private List<robochart_Event> robochart_events;




    private List<robochart_VariableList> robochart_variablelists;




    private List<robochart_Clock> robochart_clocks;




    private List<robochart_OperationSig> robochart_operationsigs;


    public robochart_BasicContext(
    ) {
        this.robochart_events = new ArrayList<>();
        this.robochart_variablelists = new ArrayList<>();
        this.robochart_clocks = new ArrayList<>();
        this.robochart_operationsigs = new ArrayList<>();
    }

    public robochart_BasicContext(
        ArrayList<robochart_Event> robochart_events,        ArrayList<robochart_VariableList> robochart_variablelists,        ArrayList<robochart_Clock> robochart_clocks,        ArrayList<robochart_OperationSig> robochart_operationsigs    ) {
        this.robochart_events = robochart_events;
        this.robochart_variablelists = robochart_variablelists;
        this.robochart_clocks = robochart_clocks;
        this.robochart_operationsigs = robochart_operationsigs;
    }


    public List<robochart_Event> getRobochart_events() {
        return robochart_events;
    }

    public void addRobochart_event(Robochart_event robochart_event) {
        this.robochart_events.add(robochart_event);
    }
    public List<robochart_VariableList> getRobochart_variablelists() {
        return robochart_variablelists;
    }

    public void addRobochart_variablelist(Robochart_variablelist robochart_variablelist) {
        this.robochart_variablelists.add(robochart_variablelist);
    }
    public List<robochart_Clock> getRobochart_clocks() {
        return robochart_clocks;
    }

    public void addRobochart_clock(Robochart_clock robochart_clock) {
        this.robochart_clocks.add(robochart_clock);
    }
    public List<robochart_OperationSig> getRobochart_operationsigs() {
        return robochart_operationsigs;
    }

    public void addRobochart_operationsig(Robochart_operationsig robochart_operationsig) {
        this.robochart_operationsigs.add(robochart_operationsig);
    }

}