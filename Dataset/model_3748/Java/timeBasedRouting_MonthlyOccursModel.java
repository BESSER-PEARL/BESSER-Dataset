




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class timeBasedRouting_MonthlyOccursModel extends OccursModel {

    private String day;
    private int skipMonths;
    private String dayOccurence;
    private boolean byIndex;
    private LocalDate startDate;
    private int dayIndex;



    public timeBasedRouting_MonthlyOccursModel(
        String day,        int skipMonths,        String dayOccurence,        boolean byIndex,        LocalDate startDate,        int dayIndex    ) {
        super(
        );
        this.day = day;
        this.skipMonths = skipMonths;
        this.dayOccurence = dayOccurence;
        this.byIndex = byIndex;
        this.startDate = startDate;
        this.dayIndex = dayIndex;
    }


    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public int getSkipmonths() {
        return skipMonths;
    }

    public void setSkipmonths(int skipMonths) {
        this.skipMonths = skipMonths;
    }
    public String getDayoccurence() {
        return dayOccurence;
    }

    public void setDayoccurence(String dayOccurence) {
        this.dayOccurence = dayOccurence;
    }
    public boolean getByindex() {
        return byIndex;
    }

    public void setByindex(boolean byIndex) {
        this.byIndex = byIndex;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getDayindex() {
        return dayIndex;
    }

    public void setDayindex(int dayIndex) {
        this.dayIndex = dayIndex;
    }


}