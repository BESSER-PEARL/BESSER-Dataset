





import java.util.List;
import java.util.ArrayList;

public class publication2014b_PublicationPhase  {

    private int minTime;
    private int maxTime;
    private String name;





    private List<publication2014b_Researcher> publication2014b_researchers;




    private publication2014b_Sequence publication2014b_sequence;




    private List<publication2014b_Rule> publication2014b_rules;




    private publication2014b_Researcher publication2014b_researcher;




    private publication2014b_PublicationProcess publication2014b_publicationprocess;




    private List<publication2014b_Sequence> publication2014b_sequences;




    private publication2014b_Sequence publication2014b_sequence;


    public publication2014b_PublicationPhase(
        int minTime,        int maxTime,        String name    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.name = name;
        this.publication2014b_researchers = new ArrayList<>();
        this.publication2014b_rules = new ArrayList<>();
        this.publication2014b_sequences = new ArrayList<>();
    }

    public publication2014b_PublicationPhase(
        int minTime,        int maxTime,        String name        ArrayList<publication2014b_Researcher> publication2014b_researchers,        ArrayList<publication2014b_Rule> publication2014b_rules,        ArrayList<publication2014b_Sequence> publication2014b_sequences    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.name = name;
        this.publication2014b_researchers = publication2014b_researchers;
        this.publication2014b_rules = publication2014b_rules;
        this.publication2014b_sequences = publication2014b_sequences;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<publication2014b_Researcher> getPublication2014b_researchers() {
        return publication2014b_researchers;
    }

    public void addPublication2014b_researcher(Publication2014b_researcher publication2014b_researcher) {
        this.publication2014b_researchers.add(publication2014b_researcher);
    }
    public publication2014b_Sequence getPublication2014b_sequence() {
        return publication2014b_sequence;
    }

    public void setPublication2014b_sequence(publication2014b_Sequence publication2014b_sequence) {
        this.publication2014b_sequence = publication2014b_sequence;
    }
    public List<publication2014b_Rule> getPublication2014b_rules() {
        return publication2014b_rules;
    }

    public void addPublication2014b_rule(Publication2014b_rule publication2014b_rule) {
        this.publication2014b_rules.add(publication2014b_rule);
    }
    public publication2014b_Researcher getPublication2014b_researcher() {
        return publication2014b_researcher;
    }

    public void setPublication2014b_researcher(publication2014b_Researcher publication2014b_researcher) {
        this.publication2014b_researcher = publication2014b_researcher;
    }
    public publication2014b_PublicationProcess getPublication2014b_publicationprocess() {
        return publication2014b_publicationprocess;
    }

    public void setPublication2014b_publicationprocess(publication2014b_PublicationProcess publication2014b_publicationprocess) {
        this.publication2014b_publicationprocess = publication2014b_publicationprocess;
    }
    public List<publication2014b_Sequence> getPublication2014b_sequences() {
        return publication2014b_sequences;
    }

    public void addPublication2014b_sequence(Publication2014b_sequence publication2014b_sequence) {
        this.publication2014b_sequences.add(publication2014b_sequence);
    }
    public publication2014b_Sequence getPublication2014b_sequence() {
        return publication2014b_sequence;
    }

    public void setPublication2014b_sequence(publication2014b_Sequence publication2014b_sequence) {
        this.publication2014b_sequence = publication2014b_sequence;
    }

}