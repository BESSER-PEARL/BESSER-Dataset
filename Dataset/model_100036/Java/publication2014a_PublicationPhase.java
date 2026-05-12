





import java.util.List;
import java.util.ArrayList;

public class publication2014a_PublicationPhase  {

    private String name;
    private int maxTime;
    private int minTime;





    private publication2014a_PublicationProcess publication2014a_publicationprocess;


    public publication2014a_PublicationPhase(
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

    public publication2014a_PublicationProcess getPublication2014a_publicationprocess() {
        return publication2014a_publicationprocess;
    }

    public void setPublication2014a_publicationprocess(publication2014a_PublicationProcess publication2014a_publicationprocess) {
        this.publication2014a_publicationprocess = publication2014a_publicationprocess;
    }

}