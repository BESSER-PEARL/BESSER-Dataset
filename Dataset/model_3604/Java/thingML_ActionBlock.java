





import java.util.List;
import java.util.ArrayList;

public class thingML_ActionBlock extends Action {






    private List<thingML_Action> thingml_actions;


    public thingML_ActionBlock(
    ) {
        super(
        );
        this.thingml_actions = new ArrayList<>();
    }

    public thingML_ActionBlock(
        ArrayList<thingML_Action> thingml_actions    ) {
        this.thingml_actions = thingml_actions;
    }


    public List<thingML_Action> getThingml_actions() {
        return thingml_actions;
    }

    public void addThingml_action(Thingml_action thingml_action) {
        this.thingml_actions.add(thingml_action);
    }

}