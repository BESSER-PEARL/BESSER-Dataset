





import java.util.List;
import java.util.ArrayList;

public class Engine  {

    private String horsePower;
    private String fuelAvg;



    public Engine(
        String horsePower,        String fuelAvg    ) {
        this.horsePower = horsePower;
        this.fuelAvg = fuelAvg;
    }


    public String getHorsepower() {
        return horsePower;
    }

    public void setHorsepower(String horsePower) {
        this.horsePower = horsePower;
    }
    public String getFuelavg() {
        return fuelAvg;
    }

    public void setFuelavg(String fuelAvg) {
        this.fuelAvg = fuelAvg;
    }


}