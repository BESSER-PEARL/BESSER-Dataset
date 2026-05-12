





import java.util.List;
import java.util.ArrayList;

public class FreightTrain  {

    private boolean containerTrain;





    private Train train;


    public FreightTrain(
        boolean containerTrain    ) {
        this.containerTrain = containerTrain;
    }


    public boolean getContainertrain() {
        return containerTrain;
    }

    public void setContainertrain(boolean containerTrain) {
        this.containerTrain = containerTrain;
    }

    public Train getTrain() {
        return train;
    }

    public void setTrain(Train train) {
        this.train = train;
    }

}