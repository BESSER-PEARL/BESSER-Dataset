




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveHistoryQuery  {

    private LocalDate toDate;
    private LocalDate fromDate;



    public LeaveHistoryQuery(
        LocalDate toDate,        LocalDate fromDate    ) {
        this.toDate = toDate;
        this.fromDate = fromDate;
    }


    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }


}