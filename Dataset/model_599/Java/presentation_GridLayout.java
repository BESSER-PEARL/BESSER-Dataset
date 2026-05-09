





import java.util.List;
import java.util.ArrayList;

public class presentation_GridLayout extends Layout {

    private String marginWidth;
    private String numColumns;
    private String makeColumnsEqualWidth;
    private String marginBottom;
    private String verticalSpacing;
    private String marginTop;
    private String horizontalSpacing;
    private String marginLeft;
    private String marginHeight;
    private String marginRight;



    public presentation_GridLayout(
        String marginWidth,        String numColumns,        String makeColumnsEqualWidth,        String marginBottom,        String verticalSpacing,        String marginTop,        String horizontalSpacing,        String marginLeft,        String marginHeight,        String marginRight    ) {
        super(
        );
        this.marginWidth = marginWidth;
        this.numColumns = numColumns;
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
        this.marginBottom = marginBottom;
        this.verticalSpacing = verticalSpacing;
        this.marginTop = marginTop;
        this.horizontalSpacing = horizontalSpacing;
        this.marginLeft = marginLeft;
        this.marginHeight = marginHeight;
        this.marginRight = marginRight;
    }


    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
    }
    public String getNumcolumns() {
        return numColumns;
    }

    public void setNumcolumns(String numColumns) {
        this.numColumns = numColumns;
    }
    public String getMakecolumnsequalwidth() {
        return makeColumnsEqualWidth;
    }

    public void setMakecolumnsequalwidth(String makeColumnsEqualWidth) {
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
    }
    public String getMarginbottom() {
        return marginBottom;
    }

    public void setMarginbottom(String marginBottom) {
        this.marginBottom = marginBottom;
    }
    public String getVerticalspacing() {
        return verticalSpacing;
    }

    public void setVerticalspacing(String verticalSpacing) {
        this.verticalSpacing = verticalSpacing;
    }
    public String getMargintop() {
        return marginTop;
    }

    public void setMargintop(String marginTop) {
        this.marginTop = marginTop;
    }
    public String getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(String horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }
    public String getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(String marginLeft) {
        this.marginLeft = marginLeft;
    }
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
    }
    public String getMarginright() {
        return marginRight;
    }

    public void setMarginright(String marginRight) {
        this.marginRight = marginRight;
    }


}