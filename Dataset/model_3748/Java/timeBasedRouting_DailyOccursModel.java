




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class timeBasedRouting_DailyOccursModel extends OccursModel {

    private LocalDate startDate;
    private int skipDays;



    public timeBasedRouting_DailyOccursModel(
        LocalDate startDate,        int skipDays    ) {
        super(
        );
        this.startDate = startDate;
        this.skipDays = skipDays;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getSkipdays() {
        return skipDays;
    }

    public void setSkipdays(int skipDays) {
        this.skipDays = skipDays;
    }


}