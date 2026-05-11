





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private boolean grabExcessHorizontalSpace;
    private int horizontalIndent;
    private int verticalSpan;
    private String horizontalAlignment;
    private String verticalAlignment;
    private int horizontalSpan;
    private boolean grabExcessVerticalSpace;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        boolean grabExcessHorizontalSpace,        int horizontalIndent,        int verticalSpan,        String horizontalAlignment,        String verticalAlignment,        int horizontalSpan,        boolean grabExcessVerticalSpace    ) {
        super(
        );
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.horizontalIndent = horizontalIndent;
        this.verticalSpan = verticalSpan;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.horizontalSpan = horizontalSpan;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }


    public boolean getGrabexcesshorizontalspace() {
        return grabExcessHorizontalSpace;
    }

    public void setGrabexcesshorizontalspace(boolean grabExcessHorizontalSpace) {
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }
    public int getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(int horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
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
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
    }
    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}