





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_WorkingShifts  {

    private String endingTime;
    private String empId;
    private String startingTime;
    private String id;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;


    public Class_Diagram_for_Proposed_system_WorkingShifts(
        String endingTime,        String empId,        String startingTime,        String id    ) {
        this.endingTime = endingTime;
        this.empId = empId;
        this.startingTime = startingTime;
        this.id = id;
    }


    public String getEndingtime() {
        return endingTime;
    }

    public void setEndingtime(String endingTime) {
        this.endingTime = endingTime;
    }
    public String getEmpid() {
        return empId;
    }

    public void setEmpid(String empId) {
        this.empId = empId;
    }
    public String getStartingtime() {
        return startingTime;
    }

    public void setStartingtime(String startingTime) {
        this.startingTime = startingTime;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Class_Diagram_for_Proposed_system_Employee getClass_diagram_for_proposed_system_employee() {
        return class_diagram_for_proposed_system_employee;
    }

    public void setClass_diagram_for_proposed_system_employee(Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employee = class_diagram_for_proposed_system_employee;
    }

}