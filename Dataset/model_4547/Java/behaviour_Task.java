





import java.util.List;
import java.util.ArrayList;

public class behaviour_Task  {






    private behaviour_TaskExecution behaviour_taskexecution;




    private behaviour_Action behaviour_action;




    private behaviour_TaskRequirement behaviour_taskrequirement;


    public behaviour_Task(
    ) {
    }



    public behaviour_TaskExecution getBehaviour_taskexecution() {
        return behaviour_taskexecution;
    }

    public void setBehaviour_taskexecution(behaviour_TaskExecution behaviour_taskexecution) {
        this.behaviour_taskexecution = behaviour_taskexecution;
    }
    public behaviour_Action getBehaviour_action() {
        return behaviour_action;
    }

    public void setBehaviour_action(behaviour_Action behaviour_action) {
        this.behaviour_action = behaviour_action;
    }
    public behaviour_TaskRequirement getBehaviour_taskrequirement() {
        return behaviour_taskrequirement;
    }

    public void setBehaviour_taskrequirement(behaviour_TaskRequirement behaviour_taskrequirement) {
        this.behaviour_taskrequirement = behaviour_taskrequirement;
    }

}