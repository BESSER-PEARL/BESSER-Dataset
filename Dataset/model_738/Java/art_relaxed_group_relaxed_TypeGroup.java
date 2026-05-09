





import java.util.List;
import java.util.ArrayList;

public class art_relaxed_group_relaxed_TypeGroup extends Group {






    private List<ComponentType> componenttypes;


    public art_relaxed_group_relaxed_TypeGroup(
    ) {
        super(
        );
        this.componenttypes = new ArrayList<>();
    }

    public art_relaxed_group_relaxed_TypeGroup(
        ArrayList<ComponentType> componenttypes    ) {
        this.componenttypes = componenttypes;
    }


    public List<ComponentType> getComponenttypes() {
        return componenttypes;
    }

    public void addComponenttype(Componenttype componenttype) {
        this.componenttypes.add(componenttype);
    }

}