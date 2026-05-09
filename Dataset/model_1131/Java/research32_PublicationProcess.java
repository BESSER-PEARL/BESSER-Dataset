





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private research32_Progress research32_progress;


    public research32_PublicationProcess(
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

    public research32_Progress getResearch32_progress() {
        return research32_progress;
    }

    public void setResearch32_progress(research32_Progress research32_progress) {
        this.research32_progress = research32_progress;
    }

}