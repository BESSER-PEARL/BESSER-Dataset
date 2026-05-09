





import java.util.List;
import java.util.ArrayList;

public class presentation_GridLayout extends Layout {

    private String marginLeft;
    private String numColumns;
    private String marginHeight;
    private String marginBottom;
    private String verticalSpacing;
    private String marginTop;
    private String marginRight;
    private String marginWidth;
    private String makeColumnsEqualWidth;
    private String horizontalSpacing;



    public presentation_GridLayout(
        String marginLeft,        String numColumns,        String marginHeight,        String marginBottom,        String verticalSpacing,        String marginTop,        String marginRight,        String marginWidth,        String makeColumnsEqualWidth,        String horizontalSpacing    ) {
        super(
        );
        this.marginLeft = marginLeft;
        this.numColumns = numColumns;
        this.marginHeight = marginHeight;
        this.marginBottom = marginBottom;
        this.verticalSpacing = verticalSpacing;
        this.marginTop = marginTop;
        this.marginRight = marginRight;
        this.marginWidth = marginWidth;
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
        this.horizontalSpacing = horizontalSpacing;
    }


    public String getMarginleft() {
        return marginLeft;
    }

    public void setMarginleft(String marginLeft) {
        this.marginLeft = marginLeft;
    }
    public String getNumcolumns() {
        return numColumns;
    }

    public void setNumcolumns(String numColumns) {
        this.numColumns = numColumns;
    }
    public String getMarginheight() {
        return marginHeight;
    }

    public void setMarginheight(String marginHeight) {
        this.marginHeight = marginHeight;
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
    public String getMarginright() {
        return marginRight;
    }

    public void setMarginright(String marginRight) {
        this.marginRight = marginRight;
    }
    public String getMarginwidth() {
        return marginWidth;
    }

    public void setMarginwidth(String marginWidth) {
        this.marginWidth = marginWidth;
    }
    public String getMakecolumnsequalwidth() {
        return makeColumnsEqualWidth;
    }

    public void setMakecolumnsequalwidth(String makeColumnsEqualWidth) {
        this.makeColumnsEqualWidth = makeColumnsEqualWidth;
    }
    public String getHorizontalspacing() {
        return horizontalSpacing;
    }

    public void setHorizontalspacing(String horizontalSpacing) {
        this.horizontalSpacing = horizontalSpacing;
    }


}