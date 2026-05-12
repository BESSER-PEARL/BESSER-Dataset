




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveHistoryQuery  {

    private LocalDate fromDate;
    private LocalDate toDate;



    public LeaveHistoryQuery(
        LocalDate fromDate,        LocalDate toDate    ) {
        this.fromDate = fromDate;
        this.toDate = toDate;
    }


    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }


}