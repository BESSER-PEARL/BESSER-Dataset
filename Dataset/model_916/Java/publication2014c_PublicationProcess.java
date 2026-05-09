





import java.util.List;
import java.util.ArrayList;

public class publication2014c_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;



    public publication2014c_PublicationProcess(
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


}