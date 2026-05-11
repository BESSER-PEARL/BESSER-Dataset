





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Rental  {

    private int untilDate;
    private int fromDate;



    public CarRental2_Rental(
        int untilDate,        int fromDate    ) {
        this.untilDate = untilDate;
        this.fromDate = fromDate;
    }


    public int getUntildate() {
        return untilDate;
    }

    public void setUntildate(int untilDate) {
        this.untilDate = untilDate;
    }
    public int getFromdate() {
        return fromDate;
    }

    public void setFromdate(int fromDate) {
        this.fromDate = fromDate;
    }


}