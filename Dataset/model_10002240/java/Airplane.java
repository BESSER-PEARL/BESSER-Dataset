





import java.util.List;
import java.util.ArrayList;

public class Airplane  {

    private int maxAttitude;
    private int maxCarryingWeight;



    public Airplane(
        int maxAttitude,        int maxCarryingWeight    ) {
        this.maxAttitude = maxAttitude;
        this.maxCarryingWeight = maxCarryingWeight;
    }


    public int getMaxattitude() {
        return maxAttitude;
    }

    public void setMaxattitude(int maxAttitude) {
        this.maxAttitude = maxAttitude;
    }
    public int getMaxcarryingweight() {
        return maxCarryingWeight;
    }

    public void setMaxcarryingweight(int maxCarryingWeight) {
        this.maxCarryingWeight = maxCarryingWeight;
    }


}