





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_overtimeRequests  {

    private String id;
    private String start_time;
    private String date;
    private String nd_time;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;


    public Class_Diagram_for_Proposed_system_overtimeRequests(
        String id,        String start_time,        String date,        String nd_time    ) {
        this.id = id;
        this.start_time = start_time;
        this.date = date;
        this.nd_time = nd_time;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStart_time() {
        return start_time;
    }

    public void setStart_time(String start_time) {
        this.start_time = start_time;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getNd_time() {
        return nd_time;
    }

    public void setNd_time(String nd_time) {
        this.nd_time = nd_time;
    }

    public Class_Diagram_for_Proposed_system_Employee getClass_diagram_for_proposed_system_employee() {
        return class_diagram_for_proposed_system_employee;
    }

    public void setClass_diagram_for_proposed_system_employee(Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employee = class_diagram_for_proposed_system_employee;
    }

}