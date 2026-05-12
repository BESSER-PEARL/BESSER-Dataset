





import java.util.List;
import java.util.ArrayList;

public class publication2014b_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private List<publication2014b_Rule> publication2014b_rules;


    public publication2014b_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014b_rules = new ArrayList<>();
    }

    public publication2014b_PublicationProcess(
        int minTime,        int maxTime        ArrayList<publication2014b_Rule> publication2014b_rules    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014b_rules = publication2014b_rules;
    }

    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }

    public List<publication2014b_Rule> getPublication2014b_rules() {
        return publication2014b_rules;
    }

    public void addPublication2014b_rule(Publication2014b_rule publication2014b_rule) {
        this.publication2014b_rules.add(publication2014b_rule);
    }

}