





import java.util.List;
import java.util.ArrayList;

public class Behaviour_WaitingLine extends Place {

    private String schedulingPolicy;





    private List<Behaviour_PostTransitionConnection> behaviour_posttransitionconnections;


    public Behaviour_WaitingLine(
        String schedulingPolicy    ) {
        super(
        );
        this.schedulingPolicy = schedulingPolicy;
        this.behaviour_posttransitionconnections = new ArrayList<>();
    }

    public Behaviour_WaitingLine(
        String schedulingPolicy        ArrayList<Behaviour_PostTransitionConnection> behaviour_posttransitionconnections    ) {
        this.schedulingPolicy = schedulingPolicy;
        this.behaviour_posttransitionconnections = behaviour_posttransitionconnections;
    }

    public String getSchedulingpolicy() {
        return schedulingPolicy;
    }

    public void setSchedulingpolicy(String schedulingPolicy) {
        this.schedulingPolicy = schedulingPolicy;
    }

    public List<Behaviour_PostTransitionConnection> getBehaviour_posttransitionconnections() {
        return behaviour_posttransitionconnections;
    }

    public void addBehaviour_posttransitionconnection(Behaviour_posttransitionconnection behaviour_posttransitionconnection) {
        this.behaviour_posttransitionconnections.add(behaviour_posttransitionconnection);
    }

}