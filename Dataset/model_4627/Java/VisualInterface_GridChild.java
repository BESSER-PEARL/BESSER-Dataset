





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_GridChild extends Child {

    private String spanRows;
    private String verticalAlignment;
    private String widthHint;
    private int spanCols;
    private boolean grabVerticalSpace;
    private boolean grabHorizontalSpace;
    private String horizontalAlignment;
    private String heightHint;



    public VisualInterface_GridChild(
        String spanRows,        String verticalAlignment,        String widthHint,        int spanCols,        boolean grabVerticalSpace,        boolean grabHorizontalSpace,        String horizontalAlignment,        String heightHint    ) {
        super(
        );
        this.spanRows = spanRows;
        this.verticalAlignment = verticalAlignment;
        this.widthHint = widthHint;
        this.spanCols = spanCols;
        this.grabVerticalSpace = grabVerticalSpace;
        this.grabHorizontalSpace = grabHorizontalSpace;
        this.horizontalAlignment = horizontalAlignment;
        this.heightHint = heightHint;
    }


    public String getSpanrows() {
        return spanRows;
    }

    public void setSpanrows(String spanRows) {
        this.spanRows = spanRows;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
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
    public boolean getGrabhorizontalspace() {
        return grabHorizontalSpace;
    }

    public void setGrabhorizontalspace(boolean grabHorizontalSpace) {
        this.grabHorizontalSpace = grabHorizontalSpace;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(String heightHint) {
        this.heightHint = heightHint;
    }


}