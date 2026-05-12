





import java.util.List;
import java.util.ArrayList;

public class Car1  {

    private String helmSide;
    private int doors;



    public Car1(
        String helmSide,        int doors    ) {
        this.helmSide = helmSide;
        this.doors = doors;
    }


    public String getHelmside() {
        return helmSide;
    }

    public void setHelmside(String helmSide) {
        this.helmSide = helmSide;
    }
    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }


}