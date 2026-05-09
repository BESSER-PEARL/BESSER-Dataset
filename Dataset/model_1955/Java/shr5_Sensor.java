





import java.util.List;
import java.util.ArrayList;

public class shr5_Sensor extends Quelle, Beschreibbar, Capacity, GeldWert {

    private int capacityValue;
    private int rating;



    public shr5_Sensor(
        int capacityValue,        int rating    ) {
        super(
        );
        this.capacityValue = capacityValue;
        this.rating = rating;
    }


    public int getCapacityvalue() {
        return capacityValue;
    }

    public void setCapacityvalue(int capacityValue) {
        this.capacityValue = capacityValue;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }


}