





import java.util.List;
import java.util.ArrayList;

public class Engine  {

    private String fuelAvg;
    private String horsePower;



    public Engine(
        String fuelAvg,        String horsePower    ) {
        this.fuelAvg = fuelAvg;
        this.horsePower = horsePower;
    }


    public String getFuelavg() {
        return fuelAvg;
    }

    public void setFuelavg(String fuelAvg) {
        this.fuelAvg = fuelAvg;
    }
    public String getHorsepower() {
        return horsePower;
    }

    public void setHorsepower(String horsePower) {
        this.horsePower = horsePower;
    }


}