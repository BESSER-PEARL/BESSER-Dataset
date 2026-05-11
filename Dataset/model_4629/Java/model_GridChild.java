





import java.util.List;
import java.util.ArrayList;

public class model_GridChild extends Child {

    private String horizontalAlignment;
    private String spanRows;
    private String heightHint;
    private boolean grabVerticalSpace;
    private String verticalAlignment;
    private String widthHint;
    private boolean grabHorizontalSpace;
    private int spanCols;



    public model_GridChild(
        String horizontalAlignment,        String spanRows,        String heightHint,        boolean grabVerticalSpace,        String verticalAlignment,        String widthHint,        boolean grabHorizontalSpace,        int spanCols    ) {
        super(
        );
        this.horizontalAlignment = horizontalAlignment;
        this.spanRows = spanRows;
        this.heightHint = heightHint;
        this.grabVerticalSpace = grabVerticalSpace;
        this.verticalAlignment = verticalAlignment;
        this.widthHint = widthHint;
        this.grabHorizontalSpace = grabHorizontalSpace;
        this.spanCols = spanCols;
    }


    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
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
    public boolean getGrabverticalspace() {
        return grabVerticalSpace;
    }

    public void setGrabverticalspace(boolean grabVerticalSpace) {
        this.grabVerticalSpace = grabVerticalSpace;
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


}