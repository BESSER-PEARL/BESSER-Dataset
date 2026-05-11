





import java.util.List;
import java.util.ArrayList;

public class behaviour_Action extends NamedElement {






    private behaviour_DynamicRobot behaviour_dynamicrobot;




    private behaviour_TaskExecution behaviour_taskexecution;


    public behaviour_Action(
    ) {
        super(
        );
    }



    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }
    public behaviour_TaskExecution getBehaviour_taskexecution() {
        return behaviour_taskexecution;
    }

    public void setBehaviour_taskexecution(behaviour_TaskExecution behaviour_taskexecution) {
        this.behaviour_taskexecution = behaviour_taskexecution;
    }

}