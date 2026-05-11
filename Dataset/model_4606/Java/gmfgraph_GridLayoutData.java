





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private String horizontalAlignment;
    private boolean grabExcessVerticalSpace;
    private int horizontalSpan;
    private boolean grabExcessHorizontalSpace;
    private String verticalAlignment;
    private int verticalSpan;
    private int horizontalIndent;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        String horizontalAlignment,        boolean grabExcessVerticalSpace,        int horizontalSpan,        boolean grabExcessHorizontalSpace,        String verticalAlignment,        int verticalSpan,        int horizontalIndent    ) {
        super(
        );
        this.horizontalAlignment = horizontalAlignment;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.horizontalSpan = horizontalSpan;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.verticalAlignment = verticalAlignment;
        this.verticalSpan = verticalSpan;
        this.horizontalIndent = horizontalIndent;
    }


    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }
    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
    }
    public boolean getGrabexcesshorizontalspace() {
        return grabExcessHorizontalSpace;
    }

    public void setGrabexcesshorizontalspace(boolean grabExcessHorizontalSpace) {
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public int getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(int verticalSpan) {
        this.verticalSpan = verticalSpan;
    }
    public int getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(int horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}