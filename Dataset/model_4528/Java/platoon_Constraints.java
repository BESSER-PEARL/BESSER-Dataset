





import java.util.List;
import java.util.ArrayList;

public class platoon_Constraints  {

    private int maxHeadway;
    private int minHeadway;





    private platoon_Model platoon_model;


    public platoon_Constraints(
        int maxHeadway,        int minHeadway    ) {
        this.maxHeadway = maxHeadway;
        this.minHeadway = minHeadway;
    }


    public int getMaxheadway() {
        return maxHeadway;
    }

    public void setMaxheadway(int maxHeadway) {
        this.maxHeadway = maxHeadway;
    }
    public int getMinheadway() {
        return minHeadway;
    }

    public void setMinheadway(int minHeadway) {
        this.minHeadway = minHeadway;
    }

    public platoon_Model getPlatoon_model() {
        return platoon_model;
    }

    public void setPlatoon_model(platoon_Model platoon_model) {
        this.platoon_model = platoon_model;
    }

}