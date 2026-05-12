





import java.util.List;
import java.util.ArrayList;

public class Engine  {

    private String type;
    private int engineSpeed;
    private int efficiencyCoefficient;



    public Engine(
        String type,        int engineSpeed,        int efficiencyCoefficient    ) {
        this.type = type;
        this.engineSpeed = engineSpeed;
        this.efficiencyCoefficient = efficiencyCoefficient;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getEnginespeed() {
        return engineSpeed;
    }

    public void setEnginespeed(int engineSpeed) {
        this.engineSpeed = engineSpeed;
    }
    public int getEfficiencycoefficient() {
        return efficiencyCoefficient;
    }

    public void setEfficiencycoefficient(int efficiencyCoefficient) {
        this.efficiencyCoefficient = efficiencyCoefficient;
    }


}