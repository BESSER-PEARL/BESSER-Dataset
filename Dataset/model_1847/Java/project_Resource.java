





import java.util.List;
import java.util.ArrayList;

public class project_Resource extends Property, ResourceAttribute {

    private String id;
    private String name;





    private project_StatusSheet project_statussheet;




    private project_BookingTask project_bookingtask;




    private project_Timesheet project_timesheet;




    private project_Alternative project_alternative;




    private project_AllocateResource project_allocateresource;




    private project_Author project_author;


    public project_Resource(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public project_StatusSheet getProject_statussheet() {
        return project_statussheet;
    }

    public void setProject_statussheet(project_StatusSheet project_statussheet) {
        this.project_statussheet = project_statussheet;
    }
    public project_BookingTask getProject_bookingtask() {
        return project_bookingtask;
    }

    public void setProject_bookingtask(project_BookingTask project_bookingtask) {
        this.project_bookingtask = project_bookingtask;
    }
    public project_Timesheet getProject_timesheet() {
        return project_timesheet;
    }

    public void setProject_timesheet(project_Timesheet project_timesheet) {
        this.project_timesheet = project_timesheet;
    }
    public project_Alternative getProject_alternative() {
        return project_alternative;
    }

    public void setProject_alternative(project_Alternative project_alternative) {
        this.project_alternative = project_alternative;
    }
    public project_AllocateResource getProject_allocateresource() {
        return project_allocateresource;
    }

    public void setProject_allocateresource(project_AllocateResource project_allocateresource) {
        this.project_allocateresource = project_allocateresource;
    }
    public project_Author getProject_author() {
        return project_author;
    }

    public void setProject_author(project_Author project_author) {
        this.project_author = project_author;
    }

}