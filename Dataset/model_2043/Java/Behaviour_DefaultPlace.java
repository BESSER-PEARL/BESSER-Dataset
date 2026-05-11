





import java.util.List;
import java.util.ArrayList;

public class Behaviour_DefaultPlace extends Place {






    private List<Behaviour_PostTransitionConnection> behaviour_posttransitionconnections;




    private List<Behaviour_PreTransitionConnection> behaviour_pretransitionconnections;


    public Behaviour_DefaultPlace(
    ) {
        super(
        );
        this.behaviour_posttransitionconnections = new ArrayList<>();
        this.behaviour_pretransitionconnections = new ArrayList<>();
    }

    public Behaviour_DefaultPlace(
        ArrayList<Behaviour_PostTransitionConnection> behaviour_posttransitionconnections,        ArrayList<Behaviour_PreTransitionConnection> behaviour_pretransitionconnections    ) {
        this.behaviour_posttransitionconnections = behaviour_posttransitionconnections;
        this.behaviour_pretransitionconnections = behaviour_pretransitionconnections;
    }


    public List<Behaviour_PostTransitionConnection> getBehaviour_posttransitionconnections() {
        return behaviour_posttransitionconnections;
    }

    public void addBehaviour_posttransitionconnection(Behaviour_posttransitionconnection behaviour_posttransitionconnection) {
        this.behaviour_posttransitionconnections.add(behaviour_posttransitionconnection);
    }
    public List<Behaviour_PreTransitionConnection> getBehaviour_pretransitionconnections() {
        return behaviour_pretransitionconnections;
    }

    public void addBehaviour_pretransitionconnection(Behaviour_pretransitionconnection behaviour_pretransitionconnection) {
        this.behaviour_pretransitionconnections.add(behaviour_pretransitionconnection);
    }

}