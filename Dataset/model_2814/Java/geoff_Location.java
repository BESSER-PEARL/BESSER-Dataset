





import java.util.List;
import java.util.ArrayList;

public class geoff_Location extends Identifiable {

    private String projectionCode;





    private geoff_View geoff_view;


    public geoff_Location(
        String projectionCode    ) {
        super(
        );
        this.projectionCode = projectionCode;
    }


    public String getProjectioncode() {
        return projectionCode;
    }

    public void setProjectioncode(String projectionCode) {
        this.projectionCode = projectionCode;
    }

    public geoff_View getGeoff_view() {
        return geoff_view;
    }

    public void setGeoff_view(geoff_View geoff_view) {
        this.geoff_view = geoff_view;
    }

}