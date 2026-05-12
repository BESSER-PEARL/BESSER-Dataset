





import java.util.List;
import java.util.ArrayList;

public class BackgroundStopLoader  {

    private String stops;





    private Car car;


    public BackgroundStopLoader(
        String stops    ) {
        this.stops = stops;
    }


    public String getStops() {
        return stops;
    }

    public void setStops(String stops) {
        this.stops = stops;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }

}