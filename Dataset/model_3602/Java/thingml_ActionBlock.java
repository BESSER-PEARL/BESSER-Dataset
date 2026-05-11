





import java.util.List;
import java.util.ArrayList;

public class thingml_ActionBlock extends Action {






    private List<thingml_Action> thingml_actions;


    public thingml_ActionBlock(
    ) {
        super(
        );
        this.thingml_actions = new ArrayList<>();
    }

    public thingml_ActionBlock(
        ArrayList<thingml_Action> thingml_actions    ) {
        this.thingml_actions = thingml_actions;
    }


    public List<thingml_Action> getThingml_actions() {
        return thingml_actions;
    }

    public void addThingml_action(Thingml_action thingml_action) {
        this.thingml_actions.add(thingml_action);
    }

}