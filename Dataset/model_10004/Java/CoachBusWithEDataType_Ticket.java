





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Ticket  {

    private int number;
    private boolean isRoundTrip;
    private float price;



    public CoachBusWithEDataType_Ticket(
        int number,        boolean isRoundTrip,        float price    ) {
        this.number = number;
        this.isRoundTrip = isRoundTrip;
        this.price = price;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
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


}