





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private int verticalSpan;
    private String horizontalAlignment;
    private int horizontalIndent;
    private int horizontalSpan;
    private String verticalAlignment;
    private boolean grabExcessVerticalSpace;
    private boolean grabExcessHorizontalSpace;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        int verticalSpan,        String horizontalAlignment,        int horizontalIndent,        int horizontalSpan,        String verticalAlignment,        boolean grabExcessVerticalSpace,        boolean grabExcessHorizontalSpace    ) {
        super(
        );
        this.verticalSpan = verticalSpan;
        this.horizontalAlignment = horizontalAlignment;
        this.horizontalIndent = horizontalIndent;
        this.horizontalSpan = horizontalSpan;
        this.verticalAlignment = verticalAlignment;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }


    public int getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(int verticalSpan) {
        this.verticalSpan = verticalSpan;
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

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}