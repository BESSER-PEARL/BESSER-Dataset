





import java.util.List;
import java.util.ArrayList;

public class tracker_WeighIn extends Event {

    private String weightGainPerDay;
    private String weight;



    public tracker_WeighIn(
        String weightGainPerDay,        String weight    ) {
        super(
        );
        this.weightGainPerDay = weightGainPerDay;
        this.weight = weight;
    }


    public String getWeightgainperday() {
        return weightGainPerDay;
    }

    public void setWeightgainperday(String weightGainPerDay) {
        this.weightGainPerDay = weightGainPerDay;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }


}