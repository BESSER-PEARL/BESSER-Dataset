





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private boolean grabExcessVerticalSpace;
    private boolean grabExcessHorizontalSpace;
    private int horizontalSpan;
    private String horizontalAlignment;
    private int verticalSpan;
    private int horizontalIndent;
    private String verticalAlignment;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        boolean grabExcessVerticalSpace,        boolean grabExcessHorizontalSpace,        int horizontalSpan,        String horizontalAlignment,        int verticalSpan,        int horizontalIndent,        String verticalAlignment    ) {
        super(
        );
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.horizontalSpan = horizontalSpan;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalSpan = verticalSpan;
        this.horizontalIndent = horizontalIndent;
        this.verticalAlignment = verticalAlignment;
    }


    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
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
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
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
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}