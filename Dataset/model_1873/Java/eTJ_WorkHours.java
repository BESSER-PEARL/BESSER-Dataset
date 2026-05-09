





import java.util.List;
import java.util.ArrayList;

public class eTJ_WorkHours  {

    private String start;
    private String stop;





    private eTJ_WorkingHours etj_workinghours;


    public eTJ_WorkHours(
        String start,        String stop    ) {
        this.start = start;
        this.stop = stop;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getStop() {
        return stop;
    }

    public void setStop(String stop) {
        this.stop = stop;
    }

    public eTJ_WorkingHours getEtj_workinghours() {
        return etj_workinghours;
    }

    public void setEtj_workinghours(eTJ_WorkingHours etj_workinghours) {
        this.etj_workinghours = etj_workinghours;
    }

}