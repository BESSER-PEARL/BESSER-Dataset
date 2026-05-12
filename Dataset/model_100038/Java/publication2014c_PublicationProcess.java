





import java.util.List;
import java.util.ArrayList;

public class publication2014c_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private List<publication2014c_Rule> publication2014c_rules;


    public publication2014c_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014c_rules = new ArrayList<>();
    }

    public publication2014c_PublicationProcess(
        int minTime,        int maxTime        ArrayList<publication2014c_Rule> publication2014c_rules    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014c_rules = publication2014c_rules;
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

    public List<publication2014c_Rule> getPublication2014c_rules() {
        return publication2014c_rules;
    }

    public void addPublication2014c_rule(Publication2014c_rule publication2014c_rule) {
        this.publication2014c_rules.add(publication2014c_rule);
    }

}