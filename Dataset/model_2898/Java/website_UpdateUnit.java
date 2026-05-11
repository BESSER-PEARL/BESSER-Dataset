





import java.util.List;
import java.util.ArrayList;

public class website_UpdateUnit extends EditUnit, SelectableUnit {

    private String styleClass;



    public website_UpdateUnit(
        String styleClass    ) {
        super(
        );
        this.styleClass = styleClass;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }


}