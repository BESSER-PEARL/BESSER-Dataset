





import java.util.List;
import java.util.ArrayList;

public class uma_PlanningData extends ProcessElement {

    private String rank;
    private String startDate;
    private String finishDate;





    private uma_BreakdownElement uma_breakdownelement;


    public uma_PlanningData(
        String rank,        String startDate,        String finishDate    ) {
        super(
        );
        this.rank = rank;
        this.startDate = startDate;
        this.finishDate = finishDate;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
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