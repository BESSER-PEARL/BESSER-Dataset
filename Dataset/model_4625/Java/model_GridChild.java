





import java.util.List;
import java.util.ArrayList;

public class model_GridChild extends Child {

    private String heightHint;
    private String horizontalAlignment;
    private boolean grabVerticalSpace;
    private boolean grabHorizontalSpace;
    private int spanCols;
    private String spanRows;
    private String verticalAlignment;
    private String widthHint;



    public model_GridChild(
        String heightHint,        String horizontalAlignment,        boolean grabVerticalSpace,        boolean grabHorizontalSpace,        int spanCols,        String spanRows,        String verticalAlignment,        String widthHint    ) {
        super(
        );
        this.heightHint = heightHint;
        this.horizontalAlignment = horizontalAlignment;
        this.grabVerticalSpace = grabVerticalSpace;
        this.grabHorizontalSpace = grabHorizontalSpace;
        this.spanCols = spanCols;
        this.spanRows = spanRows;
        this.verticalAlignment = verticalAlignment;
        this.widthHint = widthHint;
    }


    public String getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(String heightHint) {
        this.heightHint = heightHint;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
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
    public int getSpancols() {
        return spanCols;
    }

    public void setSpancols(int spanCols) {
        this.spanCols = spanCols;
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


}