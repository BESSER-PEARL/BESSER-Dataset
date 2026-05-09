





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_ActionSequence extends Action {






    private List<ardurobotml_Action> ardurobotml_actions;


    public ardurobotml_ActionSequence(
    ) {
        super(
        );
        this.ardurobotml_actions = new ArrayList<>();
    }

    public ardurobotml_ActionSequence(
        ArrayList<ardurobotml_Action> ardurobotml_actions    ) {
        this.ardurobotml_actions = ardurobotml_actions;
    }


    public List<ardurobotml_Action> getArdurobotml_actions() {
        return ardurobotml_actions;
    }

    public void addArdurobotml_action(Ardurobotml_action ardurobotml_action) {
        this.ardurobotml_actions.add(ardurobotml_action);
    }

}