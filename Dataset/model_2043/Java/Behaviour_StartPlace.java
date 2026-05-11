





import java.util.List;
import java.util.ArrayList;

public class Behaviour_StartPlace extends Place {

    private String spawnPolicy;





    private List<Behaviour_PreTransitionConnection> behaviour_pretransitionconnections;


    public Behaviour_StartPlace(
        String spawnPolicy    ) {
        super(
        );
        this.spawnPolicy = spawnPolicy;
        this.behaviour_pretransitionconnections = new ArrayList<>();
    }

    public Behaviour_StartPlace(
        String spawnPolicy        ArrayList<Behaviour_PreTransitionConnection> behaviour_pretransitionconnections    ) {
        this.spawnPolicy = spawnPolicy;
        this.behaviour_pretransitionconnections = behaviour_pretransitionconnections;
    }

    public String getSpawnpolicy() {
        return spawnPolicy;
    }

    public void setSpawnpolicy(String spawnPolicy) {
        this.spawnPolicy = spawnPolicy;
    }

    public List<Behaviour_PreTransitionConnection> getBehaviour_pretransitionconnections() {
        return behaviour_pretransitionconnections;
    }

    public void addBehaviour_pretransitionconnection(Behaviour_pretransitionconnection behaviour_pretransitionconnection) {
        this.behaviour_pretransitionconnections.add(behaviour_pretransitionconnection);
    }

}