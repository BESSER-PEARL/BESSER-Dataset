





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private boolean grabExcessHorizontalSpace;
    private int horizontalSpan;
    private String verticalAlignment;
    private String horizontalAlignment;
    private int horizontalIndent;
    private boolean grabExcessVerticalSpace;
    private int verticalSpan;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        boolean grabExcessHorizontalSpace,        int horizontalSpan,        String verticalAlignment,        String horizontalAlignment,        int horizontalIndent,        boolean grabExcessVerticalSpace,        int verticalSpan    ) {
        super(
        );
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.horizontalSpan = horizontalSpan;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.horizontalIndent = horizontalIndent;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.verticalSpan = verticalSpan;
    }


    public boolean getGrabexcesshorizontalspace() {
        return grabExcessHorizontalSpace;
    }

    public void setGrabexcesshorizontalspace(boolean grabExcessHorizontalSpace) {
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }
    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
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
    public int getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(int horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
    }
    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }
    public int getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(int verticalSpan) {
        this.verticalSpan = verticalSpan;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}