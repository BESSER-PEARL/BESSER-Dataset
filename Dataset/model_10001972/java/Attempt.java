





import java.util.List;
import java.util.ArrayList;

public class Attempt  {

    private int points;
    private int number;



    public Attempt(
        int points,        int number    ) {
        this.points = points;
        this.number = number;
    }


    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}