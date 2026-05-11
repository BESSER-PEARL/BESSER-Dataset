





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private int verticalSpan;
    private int horizontalSpan;
    private boolean grabExcessHorizontalSpace;
    private boolean grabExcessVerticalSpace;
    private int horizontalIndent;
    private String verticalAlignment;
    private String horizontalAlignment;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        int verticalSpan,        int horizontalSpan,        boolean grabExcessHorizontalSpace,        boolean grabExcessVerticalSpace,        int horizontalIndent,        String verticalAlignment,        String horizontalAlignment    ) {
        super(
        );
        this.verticalSpan = verticalSpan;
        this.horizontalSpan = horizontalSpan;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.horizontalIndent = horizontalIndent;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
    }


    public int getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(int verticalSpan) {
        this.verticalSpan = verticalSpan;
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
    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
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
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}