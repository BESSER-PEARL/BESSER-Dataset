





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Attendance  {

    private String id;
    private String attribute;
    private String clock_out;
    private String date;
    private String clock_in;
    private String empId;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;


    public Class_Diagram_for_Proposed_system_Attendance(
        String id,        String attribute,        String clock_out,        String date,        String clock_in,        String empId    ) {
        this.id = id;
        this.attribute = attribute;
        this.clock_out = clock_out;
        this.date = date;
        this.clock_in = clock_in;
        this.empId = empId;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getClock_out() {
        return clock_out;
    }

    public void setClock_out(String clock_out) {
        this.clock_out = clock_out;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getClock_in() {
        return clock_in;
    }

    public void setClock_in(String clock_in) {
        this.clock_in = clock_in;
    }
    public String getEmpid() {
        return empId;
    }

    public void setEmpid(String empId) {
        this.empId = empId;
    }

    public Class_Diagram_for_Proposed_system_Employee getClass_diagram_for_proposed_system_employee() {
        return class_diagram_for_proposed_system_employee;
    }

    public void setClass_diagram_for_proposed_system_employee(Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employee = class_diagram_for_proposed_system_employee;
    }

}