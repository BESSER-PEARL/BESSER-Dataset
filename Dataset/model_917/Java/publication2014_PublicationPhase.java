





import java.util.List;
import java.util.ArrayList;

public class publication2014_PublicationPhase  {

    private int maxTime;
    private String name;
    private int minTime;





    private publication2014_PublicationProcess publication2014_publicationprocess;


    public publication2014_PublicationPhase(
        int maxTime,        String name,        int minTime    ) {
        this.maxTime = maxTime;
        this.name = name;
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
    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }

    public publication2014_PublicationProcess getPublication2014_publicationprocess() {
        return publication2014_publicationprocess;
    }

    public void setPublication2014_publicationprocess(publication2014_PublicationProcess publication2014_publicationprocess) {
        this.publication2014_publicationprocess = publication2014_publicationprocess;
    }

}