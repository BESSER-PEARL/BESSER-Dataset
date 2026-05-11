





import java.util.List;
import java.util.ArrayList;

public class model_GridContainer extends Container {

    private boolean equalWidth;
    private int verticalSpacing;
    private int marginWidth;
    private int columns;
    private int marginHeight;
    private int horizontalSpacing;





    private List<model_GridChild> model_gridchilds;


    public model_GridContainer(
        boolean equalWidth,        int verticalSpacing,        int marginWidth,        int columns,        int marginHeight,        int horizontalSpacing    ) {
        super(
        );
        this.equalWidth = equalWidth;
        this.verticalSpacing = verticalSpacing;
        this.marginWidth = marginWidth;
        this.columns = columns;
        this.marginHeight = marginHeight;
        this.horizontalSpacing = horizontalSpacing;
        this.model_gridchilds = new ArrayList<>();
    }

    public model_GridContainer(
        boolean equalWidth,        int verticalSpacing,        int marginWidth,        int columns,        int marginHeight,        int horizontalSpacing        ArrayList<model_GridChild> model_gridchilds    ) {
        this.equalWidth = equalWidth;
        this.verticalSpacing = verticalSpacing;
        this.marginWidth = marginWidth;
        this.columns = columns;
        this.marginHeight = marginHeight;
        this.horizontalSpacing = horizontalSpacing;
        this.model_gridchilds = model_gridchilds;
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
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }

    public List<model_GridChild> getModel_gridchilds() {
        return model_gridchilds;
    }

    public void addModel_gridchild(Model_gridchild model_gridchild) {
        this.model_gridchilds.add(model_gridchild);
    }

}