




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_PlanningData extends ProcessElement {

    private String duration;
    private LocalDate startDate;
    private LocalDate finishDate;
    private int rank;





    private spem_BreakdownElement spem_breakdownelement;


    public spem_PlanningData(
        String duration,        LocalDate startDate,        LocalDate finishDate,        int rank    ) {
        super(
        );
        this.duration = duration;
        this.startDate = startDate;
        this.finishDate = finishDate;
        this.rank = rank;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getFinishdate() {
        return finishDate;
    }

    public void setFinishdate(LocalDate finishDate) {
        this.finishDate = finishDate;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public spem_BreakdownElement getSpem_breakdownelement() {
        return spem_breakdownelement;
    }

    public void setSpem_breakdownelement(spem_BreakdownElement spem_breakdownelement) {
        this.spem_breakdownelement = spem_breakdownelement;
    }

}