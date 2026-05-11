





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_XYContainer extends Container {






    private List<VisualInterface_XYChild> visualinterface_xychilds;


    public VisualInterface_XYContainer(
    ) {
        super(
        );
        this.visualinterface_xychilds = new ArrayList<>();
    }

    public VisualInterface_XYContainer(
        ArrayList<VisualInterface_XYChild> visualinterface_xychilds    ) {
        this.visualinterface_xychilds = visualinterface_xychilds;
    }


    public List<VisualInterface_XYChild> getVisualinterface_xychilds() {
        return visualinterface_xychilds;
    }

    public void addVisualinterface_xychild(Visualinterface_xychild visualinterface_xychild) {
        this.visualinterface_xychilds.add(visualinterface_xychild);
    }

}