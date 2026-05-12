





import java.util.List;
import java.util.ArrayList;

public class publication_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;



    public publication_PublicationProcess(
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


}