





import java.util.List;
import java.util.ArrayList;

public class presentation_GridData  {

    private String minimumWidth;
    private String grabExcessVerticalSpace;
    private String heightHint;
    private String exclude;
    private String grabExcessHorizontalSpace;
    private String horizontalIndent;
    private String verticalIndent;
    private String widthHint;
    private String verticalSpan;
    private String horizontalAlignment;
    private String verticalAlignment;
    private String minimumHeight;
    private String horizontalSpan;
    private String mixed;



    public presentation_GridData(
        String minimumWidth,        String grabExcessVerticalSpace,        String heightHint,        String exclude,        String grabExcessHorizontalSpace,        String horizontalIndent,        String verticalIndent,        String widthHint,        String verticalSpan,        String horizontalAlignment,        String verticalAlignment,        String minimumHeight,        String horizontalSpan,        String mixed    ) {
        this.minimumWidth = minimumWidth;
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
        this.heightHint = heightHint;
        this.exclude = exclude;
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
        this.horizontalIndent = horizontalIndent;
        this.verticalIndent = verticalIndent;
        this.widthHint = widthHint;
        this.verticalSpan = verticalSpan;
        this.horizontalAlignment = horizontalAlignment;
        this.verticalAlignment = verticalAlignment;
        this.minimumHeight = minimumHeight;
        this.horizontalSpan = horizontalSpan;
        this.mixed = mixed;
    }


    public String getMinimumwidth() {
        return minimumWidth;
    }

    public void setMinimumwidth(String minimumWidth) {
        this.minimumWidth = minimumWidth;
    }
    public String getGrabexcessverticalspace() {
        return grabExcessVerticalSpace;
    }

    public void setGrabexcessverticalspace(String grabExcessVerticalSpace) {
        this.grabExcessVerticalSpace = grabExcessVerticalSpace;
    }
    public String getHeighthint() {
        return heightHint;
    }

    public void setHeighthint(String heightHint) {
        this.heightHint = heightHint;
    }
    public String getExclude() {
        return exclude;
    }

    public void setExclude(String exclude) {
        this.exclude = exclude;
    }
    public String getGrabexcesshorizontalspace() {
        return grabExcessHorizontalSpace;
    }

    public void setGrabexcesshorizontalspace(String grabExcessHorizontalSpace) {
        this.grabExcessHorizontalSpace = grabExcessHorizontalSpace;
    }
    public String getHorizontalindent() {
        return horizontalIndent;
    }

    public void setHorizontalindent(String horizontalIndent) {
        this.horizontalIndent = horizontalIndent;
    }
    public String getVerticalindent() {
        return verticalIndent;
    }

    public void setVerticalindent(String verticalIndent) {
        this.verticalIndent = verticalIndent;
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
    public String getMinimumheight() {
        return minimumHeight;
    }

    public void setMinimumheight(String minimumHeight) {
        this.minimumHeight = minimumHeight;
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


}