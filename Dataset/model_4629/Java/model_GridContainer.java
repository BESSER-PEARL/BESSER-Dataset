





import java.util.List;
import java.util.ArrayList;

public class model_GridContainer extends Container {

    private int columns;
    private int marginWidth;
    private boolean equalWidth;
    private int horizontalSpacing;
    private int marginHeight;
    private int verticalSpacing;





    private List<model_GridChild> model_gridchilds;


    public model_GridContainer(
        int columns,        int marginWidth,        boolean equalWidth,        int horizontalSpacing,        int marginHeight,        int verticalSpacing    ) {
        super(
        );
        this.columns = columns;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.horizontalSpacing = horizontalSpacing;
        this.marginHeight = marginHeight;
        this.verticalSpacing = verticalSpacing;
        this.model_gridchilds = new ArrayList<>();
    }

    public model_GridContainer(
        int columns,        int marginWidth,        boolean equalWidth,        int horizontalSpacing,        int marginHeight,        int verticalSpacing        ArrayList<model_GridChild> model_gridchilds    ) {
        this.columns = columns;
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.horizontalSpacing = horizontalSpacing;
        this.marginHeight = marginHeight;
        this.verticalSpacing = verticalSpacing;
        this.model_gridchilds = model_gridchilds;
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
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
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

    public List<model_GridChild> getModel_gridchilds() {
        return model_gridchilds;
    }

    public void addModel_gridchild(Model_gridchild model_gridchild) {
        this.model_gridchilds.add(model_gridchild);
    }

}