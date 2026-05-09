





import java.util.List;
import java.util.ArrayList;

public class eTJ_Weekdays  {

    private String first;
    private String last;





    private eTJ_WorkingHours etj_workinghours;


    public eTJ_Weekdays(
        String first,        String last    ) {
        this.first = first;
        this.last = last;
    }


    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }
    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }

    public eTJ_WorkingHours getEtj_workinghours() {
        return etj_workinghours;
    }

    public void setEtj_workinghours(eTJ_WorkingHours etj_workinghours) {
        this.etj_workinghours = etj_workinghours;
    }

}