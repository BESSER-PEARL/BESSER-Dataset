





import java.util.List;
import java.util.ArrayList;

public class Sleeper  {

    private None builder;
    private String sleeperTrain;



    public Sleeper(
        None builder,        String sleeperTrain    ) {
        this.builder = builder;
        this.sleeperTrain = sleeperTrain;
    }


    public None getBuilder() {
        return builder;
    }

    public void setBuilder(None builder) {
        this.builder = builder;
    }
    public String getSleepertrain() {
        return sleeperTrain;
    }

    public void setSleepertrain(String sleeperTrain) {
        this.sleeperTrain = sleeperTrain;
    }


}