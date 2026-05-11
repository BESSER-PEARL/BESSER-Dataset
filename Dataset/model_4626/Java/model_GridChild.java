





import java.util.List;
import java.util.ArrayList;

public class model_GridChild extends Child {

    private String spanRows;
    private boolean grabVerticalSpace;
    private int spanCols;
    private boolean grabHorizontalSpace;
    private String verticalAlignment;
    private String horizontalAlignment;
    private String heightHint;
    private String widthHint;





    private model_GridContainer model_gridcontainer;


    public model_GridChild(
        String spanRows,        boolean grabVerticalSpace,        int spanCols,        boolean grabHorizontalSpace,        String verticalAlignment,        String horizontalAlignment,        String heightHint,        String widthHint    ) {
        super(
        );
        this.spanRows = spanRows;
        this.grabVerticalSpace = grabVerticalSpace;
        this.spanCols = spanCols;
        this.grabHorizontalSpace = grabHorizontalSpace;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.heightHint = heightHint;
        this.widthHint = widthHint;
    }


    public String getSpanrows() {
        return spanRows;
    }

    public void setSpanrows(String spanRows) {
        this.spanRows = spanRows;
    }
    public boolean getGrabverticalspace() {
        return grabVerticalSpace;
    }

    public void setGrabverticalspace(boolean grabVerticalSpace) {
        this.grabVerticalSpace = grabVerticalSpace;
    }
    public int getSpancols() {
        return spanCols;
    }

    public void setSpancols(int spanCols) {
        this.spanCols = spanCols;
    }
    public boolean getGrabhorizontalspace() {
        return grabHorizontalSpace;
    }

    public void setGrabhorizontalspace(boolean grabHorizontalSpace) {
        this.grabHorizontalSpace = grabHorizontalSpace;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
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
    public String getWidthhint() {
        return widthHint;
    }

    public void setWidthhint(String widthHint) {
        this.widthHint = widthHint;
    }

    public model_GridContainer getModel_gridcontainer() {
        return model_gridcontainer;
    }

    public void setModel_gridcontainer(model_GridContainer model_gridcontainer) {
        this.model_gridcontainer = model_gridcontainer;
    }

}