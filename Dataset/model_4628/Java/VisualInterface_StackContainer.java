





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_StackContainer extends Container {






    private List<VisualInterface_Primitive> visualinterface_primitives;


    public VisualInterface_StackContainer(
    ) {
        super(
        );
        this.visualinterface_primitives = new ArrayList<>();
    }

    public VisualInterface_StackContainer(
        ArrayList<VisualInterface_Primitive> visualinterface_primitives    ) {
        this.visualinterface_primitives = visualinterface_primitives;
    }


    public List<VisualInterface_Primitive> getVisualinterface_primitives() {
        return visualinterface_primitives;
    }

    public void addVisualinterface_primitive(Visualinterface_primitive visualinterface_primitive) {
        this.visualinterface_primitives.add(visualinterface_primitive);
    }

}