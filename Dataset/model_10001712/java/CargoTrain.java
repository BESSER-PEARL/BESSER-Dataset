





import java.util.List;
import java.util.ArrayList;

public class CargoTrain  {

    private String Stops;
    private String Origin;
    private String Containers;



    public CargoTrain(
        String Stops,        String Origin,        String Containers    ) {
        this.Stops = Stops;
        this.Origin = Origin;
        this.Containers = Containers;
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
    public String getContainers() {
        return Containers;
    }

    public void setContainers(String Containers) {
        this.Containers = Containers;
    }


}