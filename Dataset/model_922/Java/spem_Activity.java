





import java.util.List;
import java.util.ArrayList;

public class spem_Activity  {

    private int durationmax;
    private int durationmin;
    private String name;





    private spem_Process spem_process;




    private spem_Process spem_process;


    public spem_Activity(
        int durationmax,        int durationmin,        String name    ) {
        this.durationmax = durationmax;
        this.durationmin = durationmin;
        this.name = name;
    }


    public int getDurationmax() {
        return durationmax;
    }

    public void setDurationmax(int durationmax) {
        this.durationmax = durationmax;
    }
    public int getDurationmin() {
        return durationmin;
    }

    public void setDurationmin(int durationmin) {
        this.durationmin = durationmin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spem_Process getSpem_process() {
        return spem_process;
    }

    public void setSpem_process(spem_Process spem_process) {
        this.spem_process = spem_process;
    }
    public spem_Process getSpem_process() {
        return spem_process;
    }

    public void setSpem_process(spem_Process spem_process) {
        this.spem_process = spem_process;
    }

}