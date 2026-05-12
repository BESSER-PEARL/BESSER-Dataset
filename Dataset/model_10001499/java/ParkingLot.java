





import java.util.List;
import java.util.ArrayList;

public class ParkingLot  {

    private int hourlyPrice;
    private int maxSize;



    public ParkingLot(
        int hourlyPrice,        int maxSize    ) {
        this.hourlyPrice = hourlyPrice;
        this.maxSize = maxSize;
    }


    public int getHourlyprice() {
        return hourlyPrice;
    }

    public void setHourlyprice(int hourlyPrice) {
        this.hourlyPrice = hourlyPrice;
    }
    public int getMaxsize() {
        return maxSize;
    }

    public void setMaxsize(int maxSize) {
        this.maxSize = maxSize;
    }


}