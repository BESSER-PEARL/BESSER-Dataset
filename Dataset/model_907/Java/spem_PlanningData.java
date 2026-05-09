




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class spem_PlanningData extends ProcessElement {

    private int rank;
    private LocalDate startDate;
    private LocalDate finishDate;
    private String duration;





    private spem_BreakdownElement spem_breakdownelement;


    public spem_PlanningData(
        int rank,        LocalDate startDate,        LocalDate finishDate,        String duration    ) {
        super(
        );
        this.rank = rank;
        this.startDate = startDate;
        this.finishDate = finishDate;
        this.duration = duration;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
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
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public spem_BreakdownElement getSpem_breakdownelement() {
        return spem_breakdownelement;
    }

    public void setSpem_breakdownelement(spem_BreakdownElement spem_breakdownelement) {
        this.spem_breakdownelement = spem_breakdownelement;
    }

}