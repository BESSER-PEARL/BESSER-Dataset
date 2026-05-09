





import java.util.List;
import java.util.ArrayList;

public class publication2014a_PublicationPhase  {

    private int maxTime;
    private int minTime;
    private String name;



    public publication2014a_PublicationPhase(
        int maxTime,        int minTime,        String name    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}