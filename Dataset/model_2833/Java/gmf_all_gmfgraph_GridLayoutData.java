





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_GridLayoutData extends LayoutData {

    private boolean grabExcessVerticalSpace;
    private int verticalSpan;
    private int horizontalIndent;
    private String verticalAlignment;
    private String horizontalAlignment;
    private int horizontalSpan;
    private boolean grabExcessHorizontalSpace;





    private Dimension dimension;


    public gmf_all_gmfgraph_GridLayoutData(
        boolean grabExcessVerticalSpace,        int verticalSpan,        int horizontalIndent,        String verticalAlignment,        String horizontalAlignment,        int horizontalSpan,        boolean grabExcessHorizontalSpace    ) {
        super(
        );
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.verticalSpan = verticalSpan;
        this.horizontalIndent = horizontalIndent;
        this.verticalAlignment = verticalAlignment;
        this.horizontalAlignment = horizontalAlignment;
        this.horizontalSpan = horizontalSpan;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
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

    public Dimension getDimension() {
        return dimension;
    }

    public void setDimension(Dimension dimension) {
        this.dimension = dimension;
    }

}