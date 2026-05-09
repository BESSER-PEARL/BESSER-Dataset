





import java.util.List;
import java.util.ArrayList;

public class uma_PlanningData extends ProcessElement {

    private String finishDate;
    private String rank;
    private String startDate;



    public uma_PlanningData(
        String finishDate,        String rank,        String startDate    ) {
        super(
        );
        this.finishDate = finishDate;
        this.rank = rank;
        this.startDate = startDate;
    }


    public String getFinishdate() {
        return finishDate;
    }

    public void setFinishdate(String finishDate) {
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


}