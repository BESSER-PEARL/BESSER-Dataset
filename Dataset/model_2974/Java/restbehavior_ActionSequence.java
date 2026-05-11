





import java.util.List;
import java.util.ArrayList;

public class restbehavior_ActionSequence extends Action {






    private List<restbehavior_Action> restbehavior_actions;


    public restbehavior_ActionSequence(
    ) {
        super(
        );
        this.restbehavior_actions = new ArrayList<>();
    }

    public restbehavior_ActionSequence(
        ArrayList<restbehavior_Action> restbehavior_actions    ) {
        this.restbehavior_actions = restbehavior_actions;
    }


    public List<restbehavior_Action> getRestbehavior_actions() {
        return restbehavior_actions;
    }

    public void addRestbehavior_action(Restbehavior_action restbehavior_action) {
        this.restbehavior_actions.add(restbehavior_action);
    }

}