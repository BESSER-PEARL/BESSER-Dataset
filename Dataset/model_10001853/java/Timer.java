





import java.util.List;
import java.util.ArrayList;

public class Timer  {

    private int start;
    private int ticks;



    public Timer(
        int start,        int ticks    ) {
        this.start = start;
        this.ticks = ticks;
    }


    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getTicks() {
        return ticks;
    }

    public void setTicks(int ticks) {
        this.ticks = ticks;
    }


}