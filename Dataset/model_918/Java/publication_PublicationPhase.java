





import java.util.List;
import java.util.ArrayList;

public class publication_PublicationPhase  {

    private int maxTime;
    private String name;
    private int minTime;



    public publication_PublicationPhase(
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


}