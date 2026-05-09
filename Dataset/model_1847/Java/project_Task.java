





import java.util.List;
import java.util.ArrayList;

public class project_Task extends Property, TaskAttribute {

    private String name;
    private String id;





    private project_BookingResource project_bookingresource;




    private project_TaskTimesheet project_tasktimesheet;


    public project_Task(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public project_BookingResource getProject_bookingresource() {
        return project_bookingresource;
    }

    public void setProject_bookingresource(project_BookingResource project_bookingresource) {
        this.project_bookingresource = project_bookingresource;
    }
    public project_TaskTimesheet getProject_tasktimesheet() {
        return project_tasktimesheet;
    }

    public void setProject_tasktimesheet(project_TaskTimesheet project_tasktimesheet) {
        this.project_tasktimesheet = project_tasktimesheet;
    }

}