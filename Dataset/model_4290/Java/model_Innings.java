





import java.util.List;
import java.util.ArrayList;

public class model_Innings  {

    private int total;
    private String overCount;
    private int noOvers;
    private int wicketsDown;
    private String Summary;



    public model_Innings(
        int total,        String overCount,        int noOvers,        int wicketsDown,        String Summary    ) {
        this.total = total;
        this.overCount = overCount;
        this.noOvers = noOvers;
        this.wicketsDown = wicketsDown;
        this.Summary = Summary;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public String getOvercount() {
        return overCount;
    }

    public void setOvercount(String overCount) {
        this.overCount = overCount;
    }
    public int getNoovers() {
        return noOvers;
    }

    public void setNoovers(int noOvers) {
        this.noOvers = noOvers;
    }
    public int getWicketsdown() {
        return wicketsDown;
    }

    public void setWicketsdown(int wicketsDown) {
        this.wicketsDown = wicketsDown;
    }
    public String getSummary() {
        return Summary;
    }

    public void setSummary(String Summary) {
        this.Summary = Summary;
    }


}