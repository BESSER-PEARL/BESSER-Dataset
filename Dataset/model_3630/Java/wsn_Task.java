





import java.util.List;
import java.util.ArrayList;

public class wsn_Task  {

    private int priority;





    private wsn_StateMachine wsn_statemachine;




    private wsn_Message wsn_message;




    private wsn_Message wsn_message;




    private wsn_Node wsn_node;




    private wsn_Sensing wsn_sensing;




    private wsn_Timing wsn_timing;




    private wsn_Communication wsn_communication;




    private wsn_Actuating wsn_actuating;




    private wsn_Communication wsn_communication;


    public wsn_Task(
        int priority    ) {
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public wsn_StateMachine getWsn_statemachine() {
        return wsn_statemachine;
    }

    public void setWsn_statemachine(wsn_StateMachine wsn_statemachine) {
        this.wsn_statemachine = wsn_statemachine;
    }
    public wsn_Message getWsn_message() {
        return wsn_message;
    }

    public void setWsn_message(wsn_Message wsn_message) {
        this.wsn_message = wsn_message;
    }
    public wsn_Message getWsn_message() {
        return wsn_message;
    }

    public void setWsn_message(wsn_Message wsn_message) {
        this.wsn_message = wsn_message;
    }
    public wsn_Node getWsn_node() {
        return wsn_node;
    }

    public void setWsn_node(wsn_Node wsn_node) {
        this.wsn_node = wsn_node;
    }
    public wsn_Sensing getWsn_sensing() {
        return wsn_sensing;
    }

    public void setWsn_sensing(wsn_Sensing wsn_sensing) {
        this.wsn_sensing = wsn_sensing;
    }
    public wsn_Timing getWsn_timing() {
        return wsn_timing;
    }

    public void setWsn_timing(wsn_Timing wsn_timing) {
        this.wsn_timing = wsn_timing;
    }
    public wsn_Communication getWsn_communication() {
        return wsn_communication;
    }

    public void setWsn_communication(wsn_Communication wsn_communication) {
        this.wsn_communication = wsn_communication;
    }
    public wsn_Actuating getWsn_actuating() {
        return wsn_actuating;
    }

    public void setWsn_actuating(wsn_Actuating wsn_actuating) {
        this.wsn_actuating = wsn_actuating;
    }
    public wsn_Communication getWsn_communication() {
        return wsn_communication;
    }

    public void setWsn_communication(wsn_Communication wsn_communication) {
        this.wsn_communication = wsn_communication;
    }

}