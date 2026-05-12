





import java.util.List;
import java.util.ArrayList;

public class stateMachineActions_Parameters  {

    private String param;





    private stateMachineActions_EventAction statemachineactions_eventaction;




    private stateMachineActions_Parameters statemachineactions_parameters;


    public stateMachineActions_Parameters(
        String param    ) {
        this.param = param;
    }


    public String getParam() {
        return param;
    }

    public void setParam(String param) {
        this.param = param;
    }

    public stateMachineActions_EventAction getStatemachineactions_eventaction() {
        return statemachineactions_eventaction;
    }

    public void setStatemachineactions_eventaction(stateMachineActions_EventAction statemachineactions_eventaction) {
        this.statemachineactions_eventaction = statemachineactions_eventaction;
    }
    public stateMachineActions_Parameters getStatemachineactions_parameters() {
        return statemachineactions_parameters;
    }

    public void setStatemachineactions_parameters(stateMachineActions_Parameters statemachineactions_parameters) {
        this.statemachineactions_parameters = statemachineactions_parameters;
    }

}