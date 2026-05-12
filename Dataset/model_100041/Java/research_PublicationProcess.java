





import java.util.List;
import java.util.ArrayList;

public class research_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private research_PublicationSystem research_publicationsystem;


    public research_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
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

    public research_PublicationSystem getResearch_publicationsystem() {
        return research_publicationsystem;
    }

    public void setResearch_publicationsystem(research_PublicationSystem research_publicationsystem) {
        this.research_publicationsystem = research_publicationsystem;
    }

}