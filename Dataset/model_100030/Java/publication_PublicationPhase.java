





import java.util.List;
import java.util.ArrayList;

public class publication_PublicationPhase  {

    private String name;
    private int maxTime;
    private int minTime;





    private publication_PublicationProcess publication_publicationprocess;


    public publication_PublicationPhase(
        String name,        int maxTime,        int minTime    ) {
        this.name = name;
        this.maxTime = maxTime;
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
    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }

    public publication_PublicationProcess getPublication_publicationprocess() {
        return publication_publicationprocess;
    }

    public void setPublication_publicationprocess(publication_PublicationProcess publication_publicationprocess) {
        this.publication_publicationprocess = publication_publicationprocess;
    }

}