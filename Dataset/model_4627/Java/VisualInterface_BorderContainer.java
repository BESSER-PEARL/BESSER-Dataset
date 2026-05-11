





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_BorderContainer extends Container {

    private int horizontalSpacing;
    private int verticalSpacing;





    private List<VisualInterface_BorderChild> visualinterface_borderchilds;


    public VisualInterface_BorderContainer(
        int horizontalSpacing,        int verticalSpacing    ) {
        super(
        );
        this.horizontalSpacing = horizontalSpacing;
        this.verticalSpacing = verticalSpacing;
        this.visualinterface_borderchilds = new ArrayList<>();
    }

    public VisualInterface_BorderContainer(
        int horizontalSpacing,        int verticalSpacing        ArrayList<VisualInterface_BorderChild> visualinterface_borderchilds    ) {
        this.horizontalSpacing = horizontalSpacing;
        this.verticalSpacing = verticalSpacing;
        this.visualinterface_borderchilds = visualinterface_borderchilds;
    }

    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }

    public List<VisualInterface_BorderChild> getVisualinterface_borderchilds() {
        return visualinterface_borderchilds;
    }

    public void addVisualinterface_borderchild(Visualinterface_borderchild visualinterface_borderchild) {
        this.visualinterface_borderchilds.add(visualinterface_borderchild);
    }

}