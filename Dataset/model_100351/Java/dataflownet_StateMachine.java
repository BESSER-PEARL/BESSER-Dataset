





import java.util.List;
import java.util.ArrayList;

public class dataflownet_StateMachine extends Node {






    private List<dataflownet_FiringRule> dataflownet_firingrules;




    private dataflownet_StateMachineState dataflownet_statemachinestate;




    private List<dataflownet_StateMachineState> dataflownet_statemachinestates;




    private dataflownet_StateMachineState dataflownet_statemachinestate;


    public dataflownet_StateMachine(
    ) {
        super(
        );
        this.dataflownet_firingrules = new ArrayList<>();
        this.dataflownet_statemachinestates = new ArrayList<>();
    }

    public dataflownet_StateMachine(
        ArrayList<dataflownet_FiringRule> dataflownet_firingrules,        ArrayList<dataflownet_StateMachineState> dataflownet_statemachinestates    ) {
        this.dataflownet_firingrules = dataflownet_firingrules;
        this.dataflownet_statemachinestates = dataflownet_statemachinestates;
    }


    public List<dataflownet_FiringRule> getDataflownet_firingrules() {
        return dataflownet_firingrules;
    }

    public void addDataflownet_firingrule(Dataflownet_firingrule dataflownet_firingrule) {
        this.dataflownet_firingrules.add(dataflownet_firingrule);
    }
    public dataflownet_StateMachineState getDataflownet_statemachinestate() {
        return dataflownet_statemachinestate;
    }

    public void setDataflownet_statemachinestate(dataflownet_StateMachineState dataflownet_statemachinestate) {
        this.dataflownet_statemachinestate = dataflownet_statemachinestate;
    }
    public List<dataflownet_StateMachineState> getDataflownet_statemachinestates() {
        return dataflownet_statemachinestates;
    }

    public void addDataflownet_statemachinestate(Dataflownet_statemachinestate dataflownet_statemachinestate) {
        this.dataflownet_statemachinestates.add(dataflownet_statemachinestate);
    }
    public dataflownet_StateMachineState getDataflownet_statemachinestate() {
        return dataflownet_statemachinestate;
    }

    public void setDataflownet_statemachinestate(dataflownet_StateMachineState dataflownet_statemachinestate) {
        this.dataflownet_statemachinestate = dataflownet_statemachinestate;
    }

}