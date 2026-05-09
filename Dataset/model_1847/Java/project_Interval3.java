





import java.util.List;
import java.util.ArrayList;

public class project_Interval3  {

    private String start;
    private String end;





    private project_ShiftsAllocate project_shiftsallocate;




    private project_DurationQuantity project_durationquantity;




    private project_Vacation project_vacation;


    public project_Interval3(
        String start,        String end    ) {
        this.start = start;
        this.end = end;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public project_ShiftsAllocate getProject_shiftsallocate() {
        return project_shiftsallocate;
    }

    public void setProject_shiftsallocate(project_ShiftsAllocate project_shiftsallocate) {
        this.project_shiftsallocate = project_shiftsallocate;
    }
    public project_DurationQuantity getProject_durationquantity() {
        return project_durationquantity;
    }

    public void setProject_durationquantity(project_DurationQuantity project_durationquantity) {
        this.project_durationquantity = project_durationquantity;
    }
    public project_Vacation getProject_vacation() {
        return project_vacation;
    }

    public void setProject_vacation(project_Vacation project_vacation) {
        this.project_vacation = project_vacation;
    }

}