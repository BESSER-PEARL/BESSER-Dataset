





import java.util.List;
import java.util.ArrayList;

public class publication2014a_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private List<publication2014a_PublicationPhase> publication2014a_publicationphases;




    private List<publication2014a_Rule> publication2014a_rules;


    public publication2014a_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014a_publicationphases = new ArrayList<>();
        this.publication2014a_rules = new ArrayList<>();
    }

    public publication2014a_PublicationProcess(
        int minTime,        int maxTime        ArrayList<publication2014a_PublicationPhase> publication2014a_publicationphases,        ArrayList<publication2014a_Rule> publication2014a_rules    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.publication2014a_publicationphases = publication2014a_publicationphases;
        this.publication2014a_rules = publication2014a_rules;
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

    public List<publication2014a_PublicationPhase> getPublication2014a_publicationphases() {
        return publication2014a_publicationphases;
    }

    public void addPublication2014a_publicationphase(Publication2014a_publicationphase publication2014a_publicationphase) {
        this.publication2014a_publicationphases.add(publication2014a_publicationphase);
    }
    public List<publication2014a_Rule> getPublication2014a_rules() {
        return publication2014a_rules;
    }

    public void addPublication2014a_rule(Publication2014a_rule publication2014a_rule) {
        this.publication2014a_rules.add(publication2014a_rule);
    }

}