




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_PlanningData extends ProcessElement {

    private LocalDate startDate;
    private int rank;
    private String duration;
    private LocalDate finishDate;





    private spem_BreakdownElement spem_breakdownelement;


    public spem_PlanningData(
        LocalDate startDate,        int rank,        String duration,        LocalDate finishDate    ) {
        super(
        );
        this.startDate = startDate;
        this.rank = rank;
        this.duration = duration;
        this.finishDate = finishDate;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public LocalDate getFinishdate() {
        return finishDate;
    }

    public void setFinishdate(LocalDate finishDate) {
        this.finishDate = finishDate;
    }

    public spem_BreakdownElement getSpem_breakdownelement() {
        return spem_breakdownelement;
    }

    public void setSpem_breakdownelement(spem_BreakdownElement spem_breakdownelement) {
        this.spem_breakdownelement = spem_breakdownelement;
    }

}