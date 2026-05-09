





import java.util.List;
import java.util.ArrayList;

public class iritpdl_Process  {

    private String name;
    private int maxTime;
    private int minTime;



    public iritpdl_Process(
        String name,        int maxTime,        int minTime    ) {
        this.name = name;
        this.maxTime = maxTime;
        this.minTime = minTime;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}