





import java.util.List;
import java.util.ArrayList;

public class revision_PublicationPhase  {

    private String name;
    private int minTime;
    private int maxTime;





    private revision_Sequence revision_sequence;




    private revision_PublicationProcess revision_publicationprocess;




    private revision_Sequence revision_sequence;




    private List<revision_Researcher> revision_researchers;




    private revision_Researcher revision_researcher;




    private List<revision_Sequence> revision_sequences;




    private revision_PlaceHolderPP revision_placeholderpp;


    public revision_PublicationPhase(
        String name,        int minTime,        int maxTime    ) {
        this.name = name;
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.revision_researchers = new ArrayList<>();
        this.revision_sequences = new ArrayList<>();
    }

    public revision_PublicationPhase(
        String name,        int minTime,        int maxTime        ArrayList<revision_Researcher> revision_researchers,        ArrayList<revision_Sequence> revision_sequences    ) {
        this.name = name;
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.revision_researchers = revision_researchers;
        this.revision_sequences = revision_sequences;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public revision_Sequence getRevision_sequence() {
        return revision_sequence;
    }

    public void setRevision_sequence(revision_Sequence revision_sequence) {
        this.revision_sequence = revision_sequence;
    }
    public revision_PublicationProcess getRevision_publicationprocess() {
        return revision_publicationprocess;
    }

    public void setRevision_publicationprocess(revision_PublicationProcess revision_publicationprocess) {
        this.revision_publicationprocess = revision_publicationprocess;
    }
    public revision_Sequence getRevision_sequence() {
        return revision_sequence;
    }

    public void setRevision_sequence(revision_Sequence revision_sequence) {
        this.revision_sequence = revision_sequence;
    }
    public List<revision_Researcher> getRevision_researchers() {
        return revision_researchers;
    }

    public void addRevision_researcher(Revision_researcher revision_researcher) {
        this.revision_researchers.add(revision_researcher);
    }
    public revision_Researcher getRevision_researcher() {
        return revision_researcher;
    }

    public void setRevision_researcher(revision_Researcher revision_researcher) {
        this.revision_researcher = revision_researcher;
    }
    public List<revision_Sequence> getRevision_sequences() {
        return revision_sequences;
    }

    public void addRevision_sequence(Revision_sequence revision_sequence) {
        this.revision_sequences.add(revision_sequence);
    }
    public revision_PlaceHolderPP getRevision_placeholderpp() {
        return revision_placeholderpp;
    }

    public void setRevision_placeholderpp(revision_PlaceHolderPP revision_placeholderpp) {
        this.revision_placeholderpp = revision_placeholderpp;
    }

}