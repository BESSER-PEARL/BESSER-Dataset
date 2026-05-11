





import java.util.List;
import java.util.ArrayList;

public class Behavior_System extends NamedElement {






    private List<Behavior_Component> behavior_components;




    private List<Behavior_Event> behavior_events;


    public Behavior_System(
    ) {
        super(
        );
        this.behavior_components = new ArrayList<>();
        this.behavior_events = new ArrayList<>();
    }

    public Behavior_System(
        ArrayList<Behavior_Component> behavior_components,        ArrayList<Behavior_Event> behavior_events    ) {
        this.behavior_components = behavior_components;
        this.behavior_events = behavior_events;
    }


    public List<Behavior_Component> getBehavior_components() {
        return behavior_components;
    }

    public void addBehavior_component(Behavior_component behavior_component) {
        this.behavior_components.add(behavior_component);
    }
    public List<Behavior_Event> getBehavior_events() {
        return behavior_events;
    }

    public void addBehavior_event(Behavior_event behavior_event) {
        this.behavior_events.add(behavior_event);
    }

}