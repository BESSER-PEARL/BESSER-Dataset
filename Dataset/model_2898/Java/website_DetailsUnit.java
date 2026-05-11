





import java.util.List;
import java.util.ArrayList;

public class website_DetailsUnit extends SingletonUnit, DataUnit, SelectableUnit {

    private String styleClass;
    private boolean omitFieldLabels;
    private String contentClass;
    private boolean onlyDisplayWhenNotEmpty;



    public website_DetailsUnit(
        String styleClass,        boolean omitFieldLabels,        String contentClass,        boolean onlyDisplayWhenNotEmpty    ) {
        super(
        );
        this.styleClass = styleClass;
        this.omitFieldLabels = omitFieldLabels;
        this.contentClass = contentClass;
        this.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public boolean getOmitfieldlabels() {
        return omitFieldLabels;
    }

    public void setOmitfieldlabels(boolean omitFieldLabels) {
        this.omitFieldLabels = omitFieldLabels;
    }
    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public boolean getOnlydisplaywhennotempty() {
        return onlyDisplayWhenNotEmpty;
    }

    public void setOnlydisplaywhennotempty(boolean onlyDisplayWhenNotEmpty) {
        this.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty;
    }


}