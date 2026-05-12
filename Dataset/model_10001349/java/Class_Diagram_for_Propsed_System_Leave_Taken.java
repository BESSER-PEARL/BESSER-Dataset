





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Leave_Taken  {

    private int empid;
    private String enddate;
    private int id;
    private int leavetype;
    private None start_date;
    private int status;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Leave_Taken(
        int empid,        String enddate,        int id,        int leavetype,        None start_date,        int status    ) {
        this.empid = empid;
        this.enddate = enddate;
        this.id = id;
        this.leavetype = leavetype;
        this.start_date = start_date;
        this.status = status;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLeavetype() {
        return leavetype;
    }

    public void setLeavetype(int leavetype) {
        this.leavetype = leavetype;
    }
    public None getStart_date() {
        return start_date;
    }

    public void setStart_date(None start_date) {
        this.start_date = start_date;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}