




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tda593_billing_DiscountLimit  {

    private int timesLeftToUse;
    private LocalDate endDate;
    private int id;
    private LocalDate startDate;



    public tda593_billing_DiscountLimit(
        int timesLeftToUse,        LocalDate endDate,        int id,        LocalDate startDate    ) {
        this.timesLeftToUse = timesLeftToUse;
        this.endDate = endDate;
        this.id = id;
        this.startDate = startDate;
    }


    public int getTimeslefttouse() {
        return timesLeftToUse;
    }

    public void setTimeslefttouse(int timesLeftToUse) {
        this.timesLeftToUse = timesLeftToUse;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }


}