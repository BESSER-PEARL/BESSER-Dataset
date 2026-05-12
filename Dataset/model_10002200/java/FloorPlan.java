





import java.util.List;
import java.util.ArrayList;

public class FloorPlan  {

    private String floorName;





    private config config;


    public FloorPlan(
        String floorName    ) {
        this.floorName = floorName;
    }


    public String getFloorname() {
        return floorName;
    }

    public void setFloorname(String floorName) {
        this.floorName = floorName;
    }

    public config getConfig() {
        return config;
    }

    public void setConfig(config config) {
        this.config = config;
    }

}