





import java.util.List;
import java.util.ArrayList;

public class ElectricTrain  {

    private float MAXSPEED;





    private EngineCar enginecar;




    private PassengerTrain passengertrain;




    private PassengerCar passengercar;


    public ElectricTrain(
        float MAXSPEED    ) {
        this.MAXSPEED = MAXSPEED;
    }


    public float getMaxspeed() {
        return MAXSPEED;
    }

    public void setMaxspeed(float MAXSPEED) {
        this.MAXSPEED = MAXSPEED;
    }

    public EngineCar getEnginecar() {
        return enginecar;
    }

    public void setEnginecar(EngineCar enginecar) {
        this.enginecar = enginecar;
    }
    public PassengerTrain getPassengertrain() {
        return passengertrain;
    }

    public void setPassengertrain(PassengerTrain passengertrain) {
        this.passengertrain = passengertrain;
    }
    public PassengerCar getPassengercar() {
        return passengercar;
    }

    public void setPassengercar(PassengerCar passengercar) {
        this.passengercar = passengercar;
    }

}