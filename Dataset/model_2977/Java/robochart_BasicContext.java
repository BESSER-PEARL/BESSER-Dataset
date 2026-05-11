





import java.util.List;
import java.util.ArrayList;

public class robochart_BasicContext  {






    private List<robochart_OperationSig> robochart_operationsigs;




    private List<robochart_Event> robochart_events;




    private List<robochart_VariableList> robochart_variablelists;


    public robochart_BasicContext(
    ) {
        this.robochart_operationsigs = new ArrayList<>();
        this.robochart_events = new ArrayList<>();
        this.robochart_variablelists = new ArrayList<>();
    }

    public robochart_BasicContext(
        ArrayList<robochart_OperationSig> robochart_operationsigs,        ArrayList<robochart_Event> robochart_events,        ArrayList<robochart_VariableList> robochart_variablelists    ) {
        this.robochart_operationsigs = robochart_operationsigs;
        this.robochart_events = robochart_events;
        this.robochart_variablelists = robochart_variablelists;
    }


    public List<robochart_OperationSig> getRobochart_operationsigs() {
        return robochart_operationsigs;
    }

    public void addRobochart_operationsig(Robochart_operationsig robochart_operationsig) {
        this.robochart_operationsigs.add(robochart_operationsig);
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

}