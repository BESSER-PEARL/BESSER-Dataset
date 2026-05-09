





import java.util.List;
import java.util.ArrayList;

public class publication2014c_PublicationPhase  {

    private String name;
    private int minTime;
    private int maxTime;





    private publication2014c_PublicationProcess publication2014c_publicationprocess;


    public publication2014c_PublicationPhase(
        String name,        int minTime,        int maxTime    ) {
        this.name = name;
        this.minTime = minTime;
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

}