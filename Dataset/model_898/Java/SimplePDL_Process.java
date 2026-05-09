





import java.util.List;
import java.util.ArrayList;

public class SimplePDL_Process  {

    private int minTime;
    private int maxTime;
    private String name;



    public SimplePDL_Process(
        int minTime,        int maxTime,        String name    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}