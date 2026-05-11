





import java.util.List;
import java.util.ArrayList;

public class componentModel_Loop extends Action {






    private List<componentModel_Action> componentmodel_actions;


    public componentModel_Loop(
    ) {
        super(
        );
        this.componentmodel_actions = new ArrayList<>();
    }

    public componentModel_Loop(
        ArrayList<componentModel_Action> componentmodel_actions    ) {
        this.componentmodel_actions = componentmodel_actions;
    }


    public List<componentModel_Action> getComponentmodel_actions() {
        return componentmodel_actions;
    }

    public void addComponentmodel_action(Componentmodel_action componentmodel_action) {
        this.componentmodel_actions.add(componentmodel_action);
    }

}