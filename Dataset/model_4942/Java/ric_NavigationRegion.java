





import java.util.List;
import java.util.ArrayList;

public class ric_NavigationRegion  {

    private String orientation;





    private ric_HeaderRegion ric_headerregion;




    private ric_Portal ric_portal;


    public ric_NavigationRegion(
        String orientation    ) {
        this.orientation = orientation;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }

    public ric_HeaderRegion getRic_headerregion() {
        return ric_headerregion;
    }

    public void setRic_headerregion(ric_HeaderRegion ric_headerregion) {
        this.ric_headerregion = ric_headerregion;
    }
    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }

}