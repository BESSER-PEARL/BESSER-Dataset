





import java.util.List;
import java.util.ArrayList;

public class art_group_TypeGroup extends Group {






    private List<ComponentType> componenttypes;


    public art_group_TypeGroup(
    ) {
        super(
        );
        this.componenttypes = new ArrayList<>();
    }

    public art_group_TypeGroup(
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