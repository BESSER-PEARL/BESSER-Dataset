





import java.util.List;
import java.util.ArrayList;

public class Maglev  {

    private float MAXSPEED;





    private PassengerTrain passengertrain;


    public Maglev(
        float MAXSPEED    ) {
        this.MAXSPEED = MAXSPEED;
    }


    public float getMaxspeed() {
        return MAXSPEED;
    }

    public void setMaxspeed(float MAXSPEED) {
        this.MAXSPEED = MAXSPEED;
    }

    public PassengerTrain getPassengertrain() {
        return passengertrain;
    }

    public void setPassengertrain(PassengerTrain passengertrain) {
        this.passengertrain = passengertrain;
    }

}