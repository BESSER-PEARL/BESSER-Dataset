





import java.util.List;
import java.util.ArrayList;

public class Sleeper  {

    private String sleeperTrain;
    private None builder;



    public Sleeper(
        String sleeperTrain,        None builder    ) {
        this.sleeperTrain = sleeperTrain;
        this.builder = builder;
    }


    public String getSleepertrain() {
        return sleeperTrain;
    }

    public void setSleepertrain(String sleeperTrain) {
        this.sleeperTrain = sleeperTrain;
    }
    public None getBuilder() {
        return builder;
    }

    public void setBuilder(None builder) {
        this.builder = builder;
    }


}