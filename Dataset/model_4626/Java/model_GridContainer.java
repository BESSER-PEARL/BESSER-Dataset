





import java.util.List;
import java.util.ArrayList;

public class model_GridContainer extends Container {

    private int marginWidth;
    private boolean equalWidth;
    private int marginHeight;
    private int horizontalSpacing;
    private int columns;
    private int verticalSpacing;



    public model_GridContainer(
        int marginWidth,        boolean equalWidth,        int marginHeight,        int horizontalSpacing,        int columns,        int verticalSpacing    ) {
        super(
        );
        this.marginWidth = marginWidth;
        this.equalWidth = equalWidth;
        this.marginHeight = marginHeight;
        this.horizontalSpacing = horizontalSpacing;
        this.columns = columns;
        this.verticalSpacing = verticalSpacing;
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
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }


}