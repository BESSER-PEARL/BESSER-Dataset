





import java.util.List;
import java.util.ArrayList;

public class project_Shift extends Property {

    private String name;
    private String timezone;
    private String id;
    private String replace;





    private project_ShiftTimesheet project_shifttimesheet;




    private project_Shift project_shift;




    private project_Vacation project_vacation;




    private project_ShiftsAllocate project_shiftsallocate;


    public project_Shift(
        String name,        String timezone,        String id,        String replace    ) {
        super(
        );
        this.name = name;
        this.timezone = timezone;
        this.id = id;
        this.replace = replace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTimezone() {
        return timezone;
    }

    public void setTimezone(String timezone) {
        this.timezone = timezone;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getReplace() {
        return replace;
    }

    public void setReplace(String replace) {
        this.replace = replace;
    }

    public project_ShiftTimesheet getProject_shifttimesheet() {
        return project_shifttimesheet;
    }

    public void setProject_shifttimesheet(project_ShiftTimesheet project_shifttimesheet) {
        this.project_shifttimesheet = project_shifttimesheet;
    }
    public project_Shift getProject_shift() {
        return project_shift;
    }

    public void setProject_shift(project_Shift project_shift) {
        this.project_shift = project_shift;
    }
    public project_Vacation getProject_vacation() {
        return project_vacation;
    }

    public void setProject_vacation(project_Vacation project_vacation) {
        this.project_vacation = project_vacation;
    }
    public project_ShiftsAllocate getProject_shiftsallocate() {
        return project_shiftsallocate;
    }

    public void setProject_shiftsallocate(project_ShiftsAllocate project_shiftsallocate) {
        this.project_shiftsallocate = project_shiftsallocate;
    }

}