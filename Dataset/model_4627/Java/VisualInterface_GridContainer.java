





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_GridContainer extends Container {

    private int columns;
    private int horizontalSpacing;
    private int marginWidth;
    private boolean equalWidth;
    private int verticalSpacing;
    private int marginHeight;





    private List<VisualInterface_GridChild> visualinterface_gridchilds;


    public VisualInterface_GridContainer(
        int columns,        int horizontalSpacing,        int marginWidth,        boolean equalWidth,        int verticalSpacing,        int marginHeight    ) {
        super(
        );
        this.columns = columns;
        this.horizontalSpacing = horizontalSpacing;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.verticalSpacing = verticalSpacing;
        this.marginHeight = marginHeight;
        this.visualinterface_gridchilds = new ArrayList<>();
    }

    public VisualInterface_GridContainer(
        int columns,        int horizontalSpacing,        int marginWidth,        boolean equalWidth,        int verticalSpacing,        int marginHeight        ArrayList<VisualInterface_GridChild> visualinterface_gridchilds    ) {
        this.columns = columns;
        this.horizontalSpacing = horizontalSpacing;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.verticalSpacing = verticalSpacing;
        this.marginHeight = marginHeight;
        this.visualinterface_gridchilds = visualinterface_gridchilds;
    }

    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
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
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }

    public List<VisualInterface_GridChild> getVisualinterface_gridchilds() {
        return visualinterface_gridchilds;
    }

    public void addVisualinterface_gridchild(Visualinterface_gridchild visualinterface_gridchild) {
        this.visualinterface_gridchilds.add(visualinterface_gridchild);
    }

}