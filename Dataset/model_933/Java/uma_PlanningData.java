





import java.util.List;
import java.util.ArrayList;

public class uma_PlanningData extends ProcessElement {

    private String startDate;
    private String rank;
    private String finishDate;



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


}