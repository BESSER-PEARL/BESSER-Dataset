





import java.util.List;
import java.util.ArrayList;

public class swt_GridLayout  {

    private int marginBottom;
    private int marginHeight;
    private int marginWidth;
    private int marginTop;
    private int numColumns;
    private int marginLeft;
    private int horizontalSpacing;
    private boolean makeColumnsEqualWidth;
    private int marginRight;
    private int verticalSpacing;



    public swt_GridLayout(
        int marginBottom,        int marginHeight,        int marginWidth,        int marginTop,        int numColumns,        int marginLeft,        int horizontalSpacing,        boolean makeColumnsEqualWidth,        int marginRight,        int verticalSpacing    ) {
        this.marginBottom = marginBottom;
        this.marginHeight = marginHeight;
        this.marginWidth = marginWidth;
        this.marginTop = marginTop;
        this.numColumns = numColumns;
        this.marginLeft = marginLeft;
        this.horizontalSpacing = horizontalSpacing;
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
        this.marginRight = marginRight;
        this.verticalSpacing = verticalSpacing;
    }


    public int getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(int marginBottom) {
        this.marginBottom = marginBottom;
    }
    public int getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(int marginHeight) {
        this.marginHeight = marginHeight;
    }
    public int getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(int marginWidth) {
        this.marginWidth = marginWidth;
    }
    public int getMargintop() {
        return marginTop;
    }

    public void setMargintop(int marginTop) {
        this.marginTop = marginTop;
    }
    public int getNumcolumns() {
        return numColumns;
    }

    public void setNumcolumns(int numColumns) {
        this.numColumns = numColumns;
    }
    public int getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(int marginLeft) {
        this.marginLeft = marginLeft;
    }
    public int getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(int horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }
    public boolean getMakecolumnsequalwidth() {
        return makeColumnsEqualWidth;
    }

    public void setMakecolumnsequalwidth(boolean makeColumnsEqualWidth) {
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
    }
    public int getMarginright() {
        return marginRight;
    }

    public void setMarginright(int marginRight) {
        this.marginRight = marginRight;
    }
    public int getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(int verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }


}