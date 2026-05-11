





import java.util.List;
import java.util.ArrayList;

public class swt_GridData extends LayoutData {

    private int minimumWidth;
    private int horizontalIndent;
    private int verticalSpan;
    private int heightHint;
    private boolean exclude;
    private String horizontalAlignment;
    private boolean grabExcessVerticalSpace;
    private boolean grabExcessHorizontalSpace;
    private String verticalAlignment;
    private int verticalIndent;
    private int horizontalSpan;
    private int widthHint;
    private int minimumHeight;



    public swt_GridData(
        int minimumWidth,        int horizontalIndent,        int verticalSpan,        int heightHint,        boolean exclude,        String horizontalAlignment,        boolean grabExcessVerticalSpace,        boolean grabExcessHorizontalSpace,        String verticalAlignment,        int verticalIndent,        int horizontalSpan,        int widthHint,        int minimumHeight    ) {
        super(
        );
        this.minimumWidth = minimumWidth;
        this.horizontalIndent = horizontalIndent;
        this.verticalSpan = verticalSpan;
        this.heightHint = heightHint;
        this.exclude = exclude;
        this.horizontalAlignment = horizontalAlignment;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.verticalAlignment = verticalAlignment;
        this.verticalIndent = verticalIndent;
        this.horizontalSpan = horizontalSpan;
        this.widthHint = widthHint;
        this.minimumHeight = minimumHeight;
    }


    public int getMinimumwidth() {
        return minimumWidth;
    }

    public void setMinimumwidth(int minimumWidth) {
        this.minimumWidth = minimumWidth;
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
    public int getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(int heightHint) {
        this.heightHint = heightHint;
    }
    public boolean getExclude() {
        return exclude;
    }

    public void setExclude(boolean exclude) {
        this.exclude = exclude;
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
    public int getVerticalindent() {
        return verticalIndent;
    }

    public void setVerticalindent(int verticalIndent) {
        this.verticalIndent = verticalIndent;
    }
    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
    }
    public int getWidthhint() {
        return widthHint;
    }

    public void setWidthhint(int widthHint) {
        this.widthHint = widthHint;
    }
    public int getMinimumheight() {
        return minimumHeight;
    }

    public void setMinimumheight(int minimumHeight) {
        this.minimumHeight = minimumHeight;
    }


}