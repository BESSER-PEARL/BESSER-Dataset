




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class timeBasedRouting_WeeklyOccursModel extends OccursModel {

    private int skipWeeks;
    private String days;
    private LocalDate startDate;



    public timeBasedRouting_WeeklyOccursModel(
        int skipWeeks,        String days,        LocalDate startDate    ) {
        super(
        );
        this.skipWeeks = skipWeeks;
        this.days = days;
        this.startDate = startDate;
    }


    public int getSkipweeks() {
        return skipWeeks;
    }

    public void setSkipweeks(int skipWeeks) {
        this.skipWeeks = skipWeeks;
    }
    public String getDays() {
        return days;
    }

    public void setDays(String days) {
        this.days = days;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }


}