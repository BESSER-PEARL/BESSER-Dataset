





import java.util.List;
import java.util.ArrayList;

public class website_IndexUnit extends DataUnit, InlineActionContainer, CollectionUnit {

    private String rowClasses;
    private String styleClass;
    private boolean omitColumnLabels;
    private String contentClass;
    private String displayOption;



    public website_IndexUnit(
        String rowClasses,        String styleClass,        boolean omitColumnLabels,        String contentClass,        String displayOption    ) {
        super(
        );
        this.rowClasses = rowClasses;
        this.styleClass = styleClass;
        this.omitColumnLabels = omitColumnLabels;
        this.contentClass = contentClass;
        this.displayOption = displayOption;
    }


    public String getRowclasses() {
        return rowClasses;
    }

    public void setRowclasses(String rowClasses) {
        this.rowClasses = rowClasses;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public boolean getOmitcolumnlabels() {
        return omitColumnLabels;
    }

    public void setOmitcolumnlabels(boolean omitColumnLabels) {
        this.omitColumnLabels = omitColumnLabels;
    }
    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public String getDisplayoption() {
        return displayOption;
    }

    public void setDisplayoption(String displayOption) {
        this.displayOption = displayOption;
    }


}