





import java.util.List;
import java.util.ArrayList;

public class uma_PlanningData extends ProcessElement {

    private String startDate;
    private String rank;
    private String finishDate;





    private uma_BreakdownElement uma_breakdownelement;


    public uma_PlanningData(
        String startDate,        String rank,        String finishDate    ) {
        super(
        );
        this.startDate = startDate;
        this.rank = rank;
        this.finishDate = finishDate;
    }


    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public String getFinishdate() {
        return finishDate;
    }

    public void setFinishdate(String finishDate) {
        this.finishDate = finishDate;
    }

    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }

}