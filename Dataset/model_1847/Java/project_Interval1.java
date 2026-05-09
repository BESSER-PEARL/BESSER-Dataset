





import java.util.List;
import java.util.ArrayList;

public class project_Interval1  {

    private String end;
    private String start;





    private project_DurationQuantity project_durationquantity;


    public project_Interval1(
        String end,        String start    ) {
        this.end = end;
        this.start = start;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public project_DurationQuantity getProject_durationquantity() {
        return project_durationquantity;
    }

    public void setProject_durationquantity(project_DurationQuantity project_durationquantity) {
        this.project_durationquantity = project_durationquantity;
    }

}