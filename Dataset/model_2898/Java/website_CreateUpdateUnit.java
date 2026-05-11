





import java.util.List;
import java.util.ArrayList;

public class website_CreateUpdateUnit extends EditUnit, SelectableUnit {

    private String clearLabel;
    private String createUriElement;
    private String styleClass;



    public website_CreateUpdateUnit(
        String clearLabel,        String createUriElement,        String styleClass    ) {
        super(
        );
        this.clearLabel = clearLabel;
        this.createUriElement = createUriElement;
        this.styleClass = styleClass;
    }


    public String getClearlabel() {
        return clearLabel;
    }

    public void setClearlabel(String clearLabel) {
        this.clearLabel = clearLabel;
    }
    public String getCreateurielement() {
        return createUriElement;
    }

    public void setCreateurielement(String createUriElement) {
        this.createUriElement = createUriElement;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }


}