





import java.util.List;
import java.util.ArrayList;

public class presentation_GridData  {

    private String minimumWidth;
    private String horizontalIndent;
    private String exclude;
    private String minimumHeight;
    private String verticalIndent;
    private String horizontalAlignment;
    private String heightHint;
    private String verticalAlignment;
    private String grabExcessHorizontalSpace;
    private String horizontalSpan;
    private String mixed;
    private String grabExcessVerticalSpace;
    private String widthHint;
    private String verticalSpan;



    public presentation_GridData(
        String minimumWidth,        String horizontalIndent,        String exclude,        String minimumHeight,        String verticalIndent,        String horizontalAlignment,        String heightHint,        String verticalAlignment,        String grabExcessHorizontalSpace,        String horizontalSpan,        String mixed,        String grabExcessVerticalSpace,        String widthHint,        String verticalSpan    ) {
        this.minimumWidth = minimumWidth;
        this.horizontalIndent = horizontalIndent;
        this.exclude = exclude;
        this.minimumHeight = minimumHeight;
        this.verticalIndent = verticalIndent;
        this.horizontalAlignment = horizontalAlignment;
        this.heightHint = heightHint;
        this.verticalAlignment = verticalAlignment;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.horizontalSpan = horizontalSpan;
        this.mixed = mixed;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.widthHint = widthHint;
        this.verticalSpan = verticalSpan;
    }


    public String getMinimumwidth() {
        return minimumWidth;
    }

    public void setMinimumwidth(String minimumWidth) {
        this.minimumWidth = minimumWidth;
    }
    public String getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(String horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
    }
    public String getExclude() {
        return exclude;
    }

    public void setExclude(String exclude) {
        this.exclude = exclude;
    }
    public String getMinimumheight() {
        return minimumHeight;
    }

    public void setMinimumheight(String minimumHeight) {
        this.minimumHeight = minimumHeight;
    }
    public String getVerticalindent() {
        return verticalIndent;
    }

    public void setVerticalindent(String verticalIndent) {
        this.verticalIndent = verticalIndent;
    }
    public String getHorizontalalignment() {
        return horizontalAlignment;
    }

    public void setHorizontalalignment(String horizontalAlignment) {
        this.horizontalAlignment = horizontalAlignment;
    }
    public String getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(String heightHint) {
        this.heightHint = heightHint;
    }
    public String getVerticalalignment() {
        return verticalAlignment;
    }

    public void setVerticalalignment(String verticalAlignment) {
        this.verticalAlignment = verticalAlignment;
    }
    public String getGrabexcesshorizontalspace() {
        return grabExcessHorizontalSpace;
    }

    public void setGrabexcesshorizontalspace(String grabExcessHorizontalSpace) {
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }
    public String getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(String horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(String grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }
    public String getWidthhint() {
        return widthHint;
    }

    public void setWidthhint(String widthHint) {
        this.widthHint = widthHint;
    }
    public String getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(String verticalSpan) {
        this.verticalSpan = verticalSpan;
    }


}