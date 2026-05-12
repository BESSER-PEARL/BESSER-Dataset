





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_LeaveTaken  {

    private String id;
    private String attribute5;
    private String leaveDate;
    private String empId;
    private String leaveType;





    private List<Class_Diagram_for_Proposed_system_Employee> class_diagram_for_proposed_system_employees;


    public Class_Diagram_for_Proposed_system_LeaveTaken(
        String id,        String attribute5,        String leaveDate,        String empId,        String leaveType    ) {
        this.id = id;
        this.attribute5 = attribute5;
        this.leaveDate = leaveDate;
        this.empId = empId;
        this.leaveType = leaveType;
        this.class_diagram_for_proposed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Proposed_system_LeaveTaken(
        String id,        String attribute5,        String leaveDate,        String empId,        String leaveType        ArrayList<Class_Diagram_for_Proposed_system_Employee> class_diagram_for_proposed_system_employees    ) {
        this.id = id;
        this.attribute5 = attribute5;
        this.leaveDate = leaveDate;
        this.empId = empId;
        this.leaveType = leaveType;
        this.class_diagram_for_proposed_system_employees = class_diagram_for_proposed_system_employees;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAttribute5() {
        return attribute5;
    }

    public void setAttribute5(String attribute5) {
        this.attribute5 = attribute5;
    }
    public String getLeavedate() {
        return leaveDate;
    }

    public void setLeavedate(String leaveDate) {
        this.leaveDate = leaveDate;
    }
    public String getEmpid() {
        return empId;
    }

    public void setEmpid(String empId) {
        this.empId = empId;
    }
    public String getLeavetype() {
        return leaveType;
    }

    public void setLeavetype(String leaveType) {
        this.leaveType = leaveType;
    }

    public List<Class_Diagram_for_Proposed_system_Employee> getClass_diagram_for_proposed_system_employees() {
        return class_diagram_for_proposed_system_employees;
    }

    public void addClass_diagram_for_proposed_system_employee(Class_diagram_for_proposed_system_employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employees.add(class_diagram_for_proposed_system_employee);
    }

}