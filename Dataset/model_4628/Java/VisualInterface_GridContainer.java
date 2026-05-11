





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_GridContainer extends Container {

    private int columns;
    private int marginWidth;
    private boolean equalWidth;
    private int marginHeight;
    private int verticalSpacing;
    private int horizontalSpacing;





    private List<VisualInterface_GridChild> visualinterface_gridchilds;


    public VisualInterface_GridContainer(
        int columns,        int marginWidth,        boolean equalWidth,        int marginHeight,        int verticalSpacing,        int horizontalSpacing    ) {
        super(
        );
        this.columns = columns;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.marginHeight = marginHeight;
        this.verticalSpacing = verticalSpacing;
        this.horizontalSpacing = horizontalSpacing;
        this.visualinterface_gridchilds = new ArrayList<>();
    }

    public VisualInterface_GridContainer(
        int columns,        int marginWidth,        boolean equalWidth,        int marginHeight,        int verticalSpacing,        int horizontalSpacing        ArrayList<VisualInterface_GridChild> visualinterface_gridchilds    ) {
        this.columns = columns;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.marginHeight = marginHeight;
        this.verticalSpacing = verticalSpacing;
        this.horizontalSpacing = horizontalSpacing;
        this.visualinterface_gridchilds = visualinterface_gridchilds;
    }

    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public boolean getEqualwidth() {
        return equalWidth;
    }

    public void setEqualwidth(boolean equalWidth) {
        this.equalWidth = equalWidth;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }

    public List<VisualInterface_GridChild> getVisualinterface_gridchilds() {
        return visualinterface_gridchilds;
    }

    public void addVisualinterface_gridchild(Visualinterface_gridchild visualinterface_gridchild) {
        this.visualinterface_gridchilds.add(visualinterface_gridchild);
    }

}