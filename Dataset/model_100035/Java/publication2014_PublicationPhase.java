





import java.util.List;
import java.util.ArrayList;

public class publication2014_PublicationPhase  {

    private int minTime;
    private int maxTime;
    private String name;





    private publication2014_PublicationProcess publication2014_publicationprocess;




    private publication2014_Researcher publication2014_researcher;




    private publication2014_PlaceHolderPP publication2014_placeholderpp;




    private publication2014_Sequence publication2014_sequence;




    private List<publication2014_Researcher> publication2014_researchers;




    private List<publication2014_Sequence> publication2014_sequences;




    private publication2014_Sequence publication2014_sequence;


    public publication2014_PublicationPhase(
        int minTime,        int maxTime,        String name    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.name = name;
        this.publication2014_researchers = new ArrayList<>();
        this.publication2014_sequences = new ArrayList<>();
    }

    public publication2014_PublicationPhase(
        int minTime,        int maxTime,        String name        ArrayList<publication2014_Researcher> publication2014_researchers,        ArrayList<publication2014_Sequence> publication2014_sequences    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.name = name;
        this.publication2014_researchers = publication2014_researchers;
        this.publication2014_sequences = publication2014_sequences;
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

    public publication2014_PublicationProcess getPublication2014_publicationprocess() {
        return publication2014_publicationprocess;
    }

    public void setPublication2014_publicationprocess(publication2014_PublicationProcess publication2014_publicationprocess) {
        this.publication2014_publicationprocess = publication2014_publicationprocess;
    }
    public publication2014_Researcher getPublication2014_researcher() {
        return publication2014_researcher;
    }

    public void setPublication2014_researcher(publication2014_Researcher publication2014_researcher) {
        this.publication2014_researcher = publication2014_researcher;
    }
    public publication2014_PlaceHolderPP getPublication2014_placeholderpp() {
        return publication2014_placeholderpp;
    }

    public void setPublication2014_placeholderpp(publication2014_PlaceHolderPP publication2014_placeholderpp) {
        this.publication2014_placeholderpp = publication2014_placeholderpp;
    }
    public publication2014_Sequence getPublication2014_sequence() {
        return publication2014_sequence;
    }

    public void setPublication2014_sequence(publication2014_Sequence publication2014_sequence) {
        this.publication2014_sequence = publication2014_sequence;
    }
    public List<publication2014_Researcher> getPublication2014_researchers() {
        return publication2014_researchers;
    }

    public void addPublication2014_researcher(Publication2014_researcher publication2014_researcher) {
        this.publication2014_researchers.add(publication2014_researcher);
    }
    public List<publication2014_Sequence> getPublication2014_sequences() {
        return publication2014_sequences;
    }

    public void addPublication2014_sequence(Publication2014_sequence publication2014_sequence) {
        this.publication2014_sequences.add(publication2014_sequence);
    }
    public publication2014_Sequence getPublication2014_sequence() {
        return publication2014_sequence;
    }

    public void setPublication2014_sequence(publication2014_Sequence publication2014_sequence) {
        this.publication2014_sequence = publication2014_sequence;
    }

}