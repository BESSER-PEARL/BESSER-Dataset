




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class timeBasedRouting_TimeRange  {

    private String name;
    private LocalDate startRange;
    private LocalDate endRange;





    private timeBasedRouting_OccursModel timebasedrouting_occursmodel;


    public timeBasedRouting_TimeRange(
        String name,        LocalDate startRange,        LocalDate endRange    ) {
        this.name = name;
        this.startRange = startRange;
        this.endRange = endRange;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getStartrange() {
        return startRange;
    }

    public void setStartrange(LocalDate startRange) {
        this.startRange = startRange;
    }
    public LocalDate getEndrange() {
        return endRange;
    }

    public void setEndrange(LocalDate endRange) {
        this.endRange = endRange;
    }

    public timeBasedRouting_OccursModel getTimebasedrouting_occursmodel() {
        return timebasedrouting_occursmodel;
    }

    public void setTimebasedrouting_occursmodel(timeBasedRouting_OccursModel timebasedrouting_occursmodel) {
        this.timebasedrouting_occursmodel = timebasedrouting_occursmodel;
    }

}