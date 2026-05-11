





import java.util.List;
import java.util.ArrayList;

public class tracker_WeighIn extends Event {

    private String weight;
    private String weightGainPerDay;



    public tracker_WeighIn(
        String weight,        String weightGainPerDay    ) {
        super(
        );
        this.weight = weight;
        this.weightGainPerDay = weightGainPerDay;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getWeightgainperday() {
        return weightGainPerDay;
    }

    public void setWeightgainperday(String weightGainPerDay) {
        this.weightGainPerDay = weightGainPerDay;
    }


}