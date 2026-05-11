





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_GridChild extends Child {

    private String widthHint;
    private int spanCols;
    private boolean grabVerticalSpace;
    private String horizontalAlignment;
    private String verticalAlignment;
    private String spanRows;
    private String heightHint;
    private boolean grabHorizontalSpace;



    public VisualInterface_GridChild(
        String widthHint,        int spanCols,        boolean grabVerticalSpace,        String horizontalAlignment,        String verticalAlignment,        String spanRows,        String heightHint,        boolean grabHorizontalSpace    ) {
        super(
        );
        this.widthHint = widthHint;
        this.spanCols = spanCols;
        this.grabVerticalSpace = grabVerticalSpace;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.spanRows = spanRows;
        this.heightHint = heightHint;
        this.grabHorizontalSpace = grabHorizontalSpace;
    }


    public String getWidthhint() {
        return widthHint;
    }

    public void setWidthhint(String widthHint) {
        this.widthHint = widthHint;
    }
    public int getSpancols() {
        return spanCols;
    }

    public void setSpancols(int spanCols) {
        this.spanCols = spanCols;
    }
    public boolean getGrabverticalspace() {
        return grabVerticalSpace;
    }

    public void setGrabverticalspace(boolean grabVerticalSpace) {
        this.grabVerticalSpace = grabVerticalSpace;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getSpanrows() {
        return spanRows;
    }

    public void setSpanrows(String spanRows) {
        this.spanRows = spanRows;
    }
    public String getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(String heightHint) {
        this.heightHint = heightHint;
    }
    public boolean getGrabhorizontalspace() {
        return grabHorizontalSpace;
    }

    public void setGrabhorizontalspace(boolean grabHorizontalSpace) {
        this.grabHorizontalSpace = grabHorizontalSpace;
    }


}