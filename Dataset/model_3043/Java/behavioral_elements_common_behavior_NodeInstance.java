





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_common_behavior_NodeInstance extends Instance {






    private List<ComponentInstance> componentinstances;


    public behavioral_elements_common_behavior_NodeInstance(
    ) {
        super(
        );
        this.componentinstances = new ArrayList<>();
    }

    public behavioral_elements_common_behavior_NodeInstance(
        ArrayList<ComponentInstance> componentinstances    ) {
        this.componentinstances = componentinstances;
    }


    public List<ComponentInstance> getComponentinstances() {
        return componentinstances;
    }

    public void addComponentinstance(Componentinstance componentinstance) {
        this.componentinstances.add(componentinstance);
    }

}