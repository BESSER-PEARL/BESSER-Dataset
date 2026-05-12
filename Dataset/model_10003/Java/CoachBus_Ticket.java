





import java.util.List;
import java.util.ArrayList;

public class CoachBus_Ticket  {

    private boolean isRoundTrip;
    private float price;
    private int number;



    public CoachBus_Ticket(
        boolean isRoundTrip,        float price,        int number    ) {
        this.isRoundTrip = isRoundTrip;
        this.price = price;
        this.number = number;
    }


    public boolean getIsroundtrip() {
        return isRoundTrip;
    }

    public void setIsroundtrip(boolean isRoundTrip) {
        this.isRoundTrip = isRoundTrip;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}