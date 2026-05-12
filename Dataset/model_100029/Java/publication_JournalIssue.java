





import java.util.List;
import java.util.ArrayList;

public class publication_JournalIssue extends Journal {

    private String issueSupplement;
    private String volume;
    private String issue;





    private publication_JournalArticle publication_journalarticle;




    private List<publication_JournalArticle> publication_journalarticles;


    public publication_JournalIssue(
        String issueSupplement,        String volume,        String issue    ) {
        super(
        );
        this.issueSupplement = issueSupplement;
        this.volume = volume;
        this.issue = issue;
        this.publication_journalarticles = new ArrayList<>();
    }

    public publication_JournalIssue(
        String issueSupplement,        String volume,        String issue        ArrayList<publication_JournalArticle> publication_journalarticles    ) {
        this.issueSupplement = issueSupplement;
        this.volume = volume;
        this.issue = issue;
        this.publication_journalarticles = publication_journalarticles;
    }

    public String getIssuesupplement() {
        return issueSupplement;
    }

    public void setIssuesupplement(String issueSupplement) {
        this.issueSupplement = issueSupplement;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getIssue() {
        return issue;
    }

    public void setIssue(String issue) {
        this.issue = issue;
    }

    public publication_JournalArticle getPublication_journalarticle() {
        return publication_journalarticle;
    }

    public void setPublication_journalarticle(publication_JournalArticle publication_journalarticle) {
        this.publication_journalarticle = publication_journalarticle;
    }
    public List<publication_JournalArticle> getPublication_journalarticles() {
        return publication_journalarticles;
    }

    public void addPublication_journalarticle(Publication_journalarticle publication_journalarticle) {
        this.publication_journalarticles.add(publication_journalarticle);
    }

}