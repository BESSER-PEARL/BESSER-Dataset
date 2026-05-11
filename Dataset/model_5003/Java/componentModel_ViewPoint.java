





import java.util.List;
import java.util.ArrayList;

public class componentModel_ViewPoint  {






    private List<componentModel_ViewType> componentmodel_viewtypes;


    public componentModel_ViewPoint(
    ) {
        this.componentmodel_viewtypes = new ArrayList<>();
    }

    public componentModel_ViewPoint(
        ArrayList<componentModel_ViewType> componentmodel_viewtypes    ) {
        this.componentmodel_viewtypes = componentmodel_viewtypes;
    }


    public List<componentModel_ViewType> getComponentmodel_viewtypes() {
        return componentmodel_viewtypes;
    }

    public void addComponentmodel_viewtype(Componentmodel_viewtype componentmodel_viewtype) {
        this.componentmodel_viewtypes.add(componentmodel_viewtype);
    }

}