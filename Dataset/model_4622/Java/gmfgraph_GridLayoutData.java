





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayoutData extends LayoutData {

    private int horizontalSpan;
    private String horizontalAlignment;
    private int verticalSpan;
    private boolean grabExcessVerticalSpace;
    private String verticalAlignment;
    private int horizontalIndent;
    private boolean grabExcessHorizontalSpace;





    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayoutData(
        int horizontalSpan,        String horizontalAlignment,        int verticalSpan,        boolean grabExcessVerticalSpace,        String verticalAlignment,        int horizontalIndent,        boolean grabExcessHorizontalSpace    ) {
        super(
        );
        this.horizontalSpan = horizontalSpan;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalSpan = verticalSpan;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.verticalAlignment = verticalAlignment;
        this.horizontalIndent = horizontalIndent;
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
    public boolean getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(boolean grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public int getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(int horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
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