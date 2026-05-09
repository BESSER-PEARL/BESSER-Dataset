





import java.util.List;
import java.util.ArrayList;

public class research15_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private research15_Progress research15_progress;


    public research15_PublicationProcess(
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

    public research15_Progress getResearch15_progress() {
        return research15_progress;
    }

    public void setResearch15_progress(research15_Progress research15_progress) {
        this.research15_progress = research15_progress;
    }

}