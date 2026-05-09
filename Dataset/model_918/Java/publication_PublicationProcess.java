





import java.util.List;
import java.util.ArrayList;

public class publication_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private List<publication_PublicationPhase> publication_publicationphases;


    public publication_PublicationProcess(
        int maxTime,        int minTime    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.publication_publicationphases = new ArrayList<>();
    }

    public publication_PublicationProcess(
        int maxTime,        int minTime        ArrayList<publication_PublicationPhase> publication_publicationphases    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.publication_publicationphases = publication_publicationphases;
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

    public List<publication_PublicationPhase> getPublication_publicationphases() {
        return publication_publicationphases;
    }

    public void addPublication_publicationphase(Publication_publicationphase publication_publicationphase) {
        this.publication_publicationphases.add(publication_publicationphase);
    }

}