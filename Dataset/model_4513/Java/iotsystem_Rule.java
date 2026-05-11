





import java.util.List;
import java.util.ArrayList;

public class iotsystem_Rule extends NamedElement {






    private List<iotsystem_Action> iotsystem_actions;




    private iotsystem_Condition iotsystem_condition;


    public iotsystem_Rule(
    ) {
        super(
        );
        this.iotsystem_actions = new ArrayList<>();
    }

    public iotsystem_Rule(
        ArrayList<iotsystem_Action> iotsystem_actions    ) {
        this.iotsystem_actions = iotsystem_actions;
    }


    public List<iotsystem_Action> getIotsystem_actions() {
        return iotsystem_actions;
    }

    public void addIotsystem_action(Iotsystem_action iotsystem_action) {
        this.iotsystem_actions.add(iotsystem_action);
    }
    public iotsystem_Condition getIotsystem_condition() {
        return iotsystem_condition;
    }

    public void setIotsystem_condition(iotsystem_Condition iotsystem_condition) {
        this.iotsystem_condition = iotsystem_condition;
    }

}