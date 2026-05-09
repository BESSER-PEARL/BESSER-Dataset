





import java.util.List;
import java.util.ArrayList;

public class publication2014b_PublicationPhase  {

    private int maxTime;
    private int minTime;
    private String name;





    private publication2014b_Sequence publication2014b_sequence;




    private List<publication2014b_Researcher> publication2014b_researchers;




    private publication2014b_PublicationProcess publication2014b_publicationprocess;




    private publication2014b_Sequence publication2014b_sequence;




    private publication2014b_Researcher publication2014b_researcher;




    private List<publication2014b_Rule> publication2014b_rules;




    private List<publication2014b_Sequence> publication2014b_sequences;


    public publication2014b_PublicationPhase(
        int maxTime,        int minTime,        String name    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.name = name;
        this.publication2014b_researchers = new ArrayList<>();
        this.publication2014b_rules = new ArrayList<>();
        this.publication2014b_sequences = new ArrayList<>();
    }

    public publication2014b_PublicationPhase(
        int maxTime,        int minTime,        String name        ArrayList<publication2014b_Researcher> publication2014b_researchers,        ArrayList<publication2014b_Rule> publication2014b_rules,        ArrayList<publication2014b_Sequence> publication2014b_sequences    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.name = name;
        this.publication2014b_researchers = publication2014b_researchers;
        this.publication2014b_rules = publication2014b_rules;
        this.publication2014b_sequences = publication2014b_sequences;
    }

    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
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

    public publication2014b_Sequence getPublication2014b_sequence() {
        return publication2014b_sequence;
    }

    public void setPublication2014b_sequence(publication2014b_Sequence publication2014b_sequence) {
        this.publication2014b_sequence = publication2014b_sequence;
    }
    public List<publication2014b_Researcher> getPublication2014b_researchers() {
        return publication2014b_researchers;
    }

    public void addPublication2014b_researcher(Publication2014b_researcher publication2014b_researcher) {
        this.publication2014b_researchers.add(publication2014b_researcher);
    }
    public publication2014b_PublicationProcess getPublication2014b_publicationprocess() {
        return publication2014b_publicationprocess;
    }

    public void setPublication2014b_publicationprocess(publication2014b_PublicationProcess publication2014b_publicationprocess) {
        this.publication2014b_publicationprocess = publication2014b_publicationprocess;
    }
    public publication2014b_Sequence getPublication2014b_sequence() {
        return publication2014b_sequence;
    }

    public void setPublication2014b_sequence(publication2014b_Sequence publication2014b_sequence) {
        this.publication2014b_sequence = publication2014b_sequence;
    }
    public publication2014b_Researcher getPublication2014b_researcher() {
        return publication2014b_researcher;
    }

    public void setPublication2014b_researcher(publication2014b_Researcher publication2014b_researcher) {
        this.publication2014b_researcher = publication2014b_researcher;
    }
    public List<publication2014b_Rule> getPublication2014b_rules() {
        return publication2014b_rules;
    }

    public void addPublication2014b_rule(Publication2014b_rule publication2014b_rule) {
        this.publication2014b_rules.add(publication2014b_rule);
    }
    public List<publication2014b_Sequence> getPublication2014b_sequences() {
        return publication2014b_sequences;
    }

    public void addPublication2014b_sequence(Publication2014b_sequence publication2014b_sequence) {
        this.publication2014b_sequences.add(publication2014b_sequence);
    }

}