





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_Chart extends State {






    private StateflowMachine stateflowmachine;




    private stateflow_simulink_ChartBlock stateflow_simulink_chartblock;


    public simulink_stateflow_Chart(
    ) {
        super(
        );
    }



    public StateflowMachine getStateflowmachine() {
        return stateflowmachine;
    }

    public void setStateflowmachine(StateflowMachine stateflowmachine) {
        this.stateflowmachine = stateflowmachine;
    }
    public stateflow_simulink_ChartBlock getStateflow_simulink_chartblock() {
        return stateflow_simulink_chartblock;
    }

    public void setStateflow_simulink_chartblock(stateflow_simulink_ChartBlock stateflow_simulink_chartblock) {
        this.stateflow_simulink_chartblock = stateflow_simulink_chartblock;
    }

}