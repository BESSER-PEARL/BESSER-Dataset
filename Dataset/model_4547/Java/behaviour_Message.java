




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class behaviour_Message extends NamedElement {

    private boolean needResponse;
    private LocalDate timestamp;





    private List<behaviour_TaskExecution> behaviour_taskexecutions;




    private behaviour_Message behaviour_message;


    public behaviour_Message(
        boolean needResponse,        LocalDate timestamp    ) {
        super(
        );
        this.needResponse = needResponse;
        this.timestamp = timestamp;
        this.behaviour_taskexecutions = new ArrayList<>();
    }

    public behaviour_Message(
        boolean needResponse,        LocalDate timestamp        ArrayList<behaviour_TaskExecution> behaviour_taskexecutions    ) {
        this.needResponse = needResponse;
        this.timestamp = timestamp;
        this.behaviour_taskexecutions = behaviour_taskexecutions;
    }

    public boolean getNeedresponse() {
        return needResponse;
    }

    public void setNeedresponse(boolean needResponse) {
        this.needResponse = needResponse;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }

    public List<behaviour_TaskExecution> getBehaviour_taskexecutions() {
        return behaviour_taskexecutions;
    }

    public void addBehaviour_taskexecution(Behaviour_taskexecution behaviour_taskexecution) {
        this.behaviour_taskexecutions.add(behaviour_taskexecution);
    }
    public behaviour_Message getBehaviour_message() {
        return behaviour_message;
    }

    public void setBehaviour_message(behaviour_Message behaviour_message) {
        this.behaviour_message = behaviour_message;
    }

}