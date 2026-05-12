





import java.util.List;
import java.util.ArrayList;

public class ParkingLot  {

    private int maxSize;
    private int hourlyPrice;



    public ParkingLot(
        int maxSize,        int hourlyPrice    ) {
        this.maxSize = maxSize;
        this.hourlyPrice = hourlyPrice;
    }


    public int getMaxsize() {
        return maxSize;
    }

    public void setMaxsize(int maxSize) {
        this.maxSize = maxSize;
    }
    public int getHourlyprice() {
        return hourlyPrice;
    }

    public void setHourlyprice(int hourlyPrice) {
        this.hourlyPrice = hourlyPrice;
    }


}