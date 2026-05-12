





import java.util.List;
import java.util.ArrayList;

public class research31_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private research31_PublicationSystem research31_publicationsystem;




    private research31_Progress research31_progress;


    public research31_PublicationProcess(
        int maxTime,        int minTime    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
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

    public research31_PublicationSystem getResearch31_publicationsystem() {
        return research31_publicationsystem;
    }

    public void setResearch31_publicationsystem(research31_PublicationSystem research31_publicationsystem) {
        this.research31_publicationsystem = research31_publicationsystem;
    }
    public research31_Progress getResearch31_progress() {
        return research31_progress;
    }

    public void setResearch31_progress(research31_Progress research31_progress) {
        this.research31_progress = research31_progress;
    }

}