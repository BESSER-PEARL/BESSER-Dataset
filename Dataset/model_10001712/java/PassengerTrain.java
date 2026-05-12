





import java.util.List;
import java.util.ArrayList;

public class PassengerTrain  {

    private String Stops;
    private String Origin;
    private int numberOfPassengers;



    public PassengerTrain(
        String Stops,        String Origin,        int numberOfPassengers    ) {
        this.Stops = Stops;
        this.Origin = Origin;
        this.numberOfPassengers = numberOfPassengers;
    }


    public String getStops() {
        return Stops;
    }

    public void setStops(String Stops) {
        this.Stops = Stops;
    }
    public String getOrigin() {
        return Origin;
    }

    public void setOrigin(String Origin) {
        this.Origin = Origin;
    }
    public int getNumberofpassengers() {
        return numberOfPassengers;
    }

    public void setNumberofpassengers(int numberOfPassengers) {
        this.numberOfPassengers = numberOfPassengers;
    }


}