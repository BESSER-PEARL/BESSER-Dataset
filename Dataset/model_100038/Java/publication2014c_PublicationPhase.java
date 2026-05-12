





import java.util.List;
import java.util.ArrayList;

public class publication2014c_PublicationPhase  {

    private int minTime;
    private String name;
    private int maxTime;





    private publication2014c_PublicationProcess publication2014c_publicationprocess;




    private List<publication2014c_Sequence> publication2014c_sequences;




    private List<publication2014c_Rule> publication2014c_rules;




    private publication2014c_Sequence publication2014c_sequence;




    private publication2014c_Sequence publication2014c_sequence;


    public publication2014c_PublicationPhase(
        int minTime,        String name,        int maxTime    ) {
        this.minTime = minTime;
        this.name = name;
        this.maxTime = maxTime;
        this.publication2014c_sequences = new ArrayList<>();
        this.publication2014c_rules = new ArrayList<>();
    }

    public publication2014c_PublicationPhase(
        int minTime,        String name,        int maxTime        ArrayList<publication2014c_Sequence> publication2014c_sequences,        ArrayList<publication2014c_Rule> publication2014c_rules    ) {
        this.minTime = minTime;
        this.name = name;
        this.maxTime = maxTime;
        this.publication2014c_sequences = publication2014c_sequences;
        this.publication2014c_rules = publication2014c_rules;
    }

    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }

    public publication2014c_PublicationProcess getPublication2014c_publicationprocess() {
        return publication2014c_publicationprocess;
    }

    public void setPublication2014c_publicationprocess(publication2014c_PublicationProcess publication2014c_publicationprocess) {
        this.publication2014c_publicationprocess = publication2014c_publicationprocess;
    }
    public List<publication2014c_Sequence> getPublication2014c_sequences() {
        return publication2014c_sequences;
    }

    public void addPublication2014c_sequence(Publication2014c_sequence publication2014c_sequence) {
        this.publication2014c_sequences.add(publication2014c_sequence);
    }
    public List<publication2014c_Rule> getPublication2014c_rules() {
        return publication2014c_rules;
    }

    public void addPublication2014c_rule(Publication2014c_rule publication2014c_rule) {
        this.publication2014c_rules.add(publication2014c_rule);
    }
    public publication2014c_Sequence getPublication2014c_sequence() {
        return publication2014c_sequence;
    }

    public void setPublication2014c_sequence(publication2014c_Sequence publication2014c_sequence) {
        this.publication2014c_sequence = publication2014c_sequence;
    }
    public publication2014c_Sequence getPublication2014c_sequence() {
        return publication2014c_sequence;
    }

    public void setPublication2014c_sequence(publication2014c_Sequence publication2014c_sequence) {
        this.publication2014c_sequence = publication2014c_sequence;
    }

}