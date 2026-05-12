





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Leave_Taken  {

    private int status;
    private int id;
    private String start_date;
    private int empid;
    private String enddate;
    private int leavetype;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Leave_Taken(
        int status,        int id,        String start_date,        int empid,        String enddate,        int leavetype    ) {
        this.status = status;
        this.id = id;
        this.start_date = start_date;
        this.empid = empid;
        this.enddate = enddate;
        this.leavetype = leavetype;
    }


    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getStart_date() {
        return start_date;
    }

    public void setStart_date(String start_date) {
        this.start_date = start_date;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public String getEnddate() {
        return enddate;
    }

    public void setEnddate(String enddate) {
        this.enddate = enddate;
    }
    public int getLeavetype() {
        return leavetype;
    }

    public void setLeavetype(int leavetype) {
        this.leavetype = leavetype;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}