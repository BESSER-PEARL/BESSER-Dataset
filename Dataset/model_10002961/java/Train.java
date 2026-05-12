





import java.util.List;
import java.util.ArrayList;

public class Train  {

    private int totalCars;
    private float milesPerHour;



    public Train(
        int totalCars,        float milesPerHour    ) {
        this.totalCars = totalCars;
        this.milesPerHour = milesPerHour;
    }


    public int getTotalcars() {
        return totalCars;
    }

    public void setTotalcars(int totalCars) {
        this.totalCars = totalCars;
    }
    public float getMilesperhour() {
        return milesPerHour;
    }

    public void setMilesperhour(float milesPerHour) {
        this.milesPerHour = milesPerHour;
    }


}