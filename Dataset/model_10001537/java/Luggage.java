





import java.util.List;
import java.util.ArrayList;

public class Luggage  {

    private int weight;





    private CheckStaff checkstaff;


    public Luggage(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public CheckStaff getCheckstaff() {
        return checkstaff;
    }

    public void setCheckstaff(CheckStaff checkstaff) {
        this.checkstaff = checkstaff;
    }

}