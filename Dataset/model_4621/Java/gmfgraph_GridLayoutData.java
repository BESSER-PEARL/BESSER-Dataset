





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private int horizontalSpan;
    private int horizontalIndent;
    private int verticalSpan;
    private boolean grabExcessHorizontalSpace;
    private String verticalAlignment;
    private String horizontalAlignment;
    private boolean grabExcessVerticalSpace;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        int horizontalSpan,        int horizontalIndent,        int verticalSpan,        boolean grabExcessHorizontalSpace,        String verticalAlignment,        String horizontalAlignment,        boolean grabExcessVerticalSpace    ) {
        super(
        );
        this.horizontalSpan = horizontalSpan;
        this.horizontalIndent = horizontalIndent;
        this.verticalSpan = verticalSpan;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }


    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
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

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}