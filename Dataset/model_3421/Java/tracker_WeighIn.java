





import java.util.List;
import java.util.ArrayList;

public class tracker_WeighIn extends Event {

    private int weight;



    public tracker_WeighIn(
        int weight    ) {
        super(
        );
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


}