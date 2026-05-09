





import java.util.List;
import java.util.ArrayList;

public class uma_PlanningData extends ProcessElement {

    private String rank;
    private String finishDate;
    private String startDate;



    public uma_PlanningData(
        String rank,        String finishDate,        String startDate    ) {
        super(
        );
        this.rank = rank;
        this.finishDate = finishDate;
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
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }


}