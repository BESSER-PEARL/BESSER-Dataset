





import java.util.List;
import java.util.ArrayList;

public class CarRental_Rental  {

    private String untilDate;
    private String framDate;



    public CarRental_Rental(
        String untilDate,        String framDate    ) {
        this.untilDate = untilDate;
        this.framDate = framDate;
    }


    public String getUntildate() {
        return untilDate;
    }

    public void setUntildate(String untilDate) {
        this.untilDate = untilDate;
    }
    public String getFramdate() {
        return framDate;
    }

    public void setFramdate(String framDate) {
        this.framDate = framDate;
    }


}