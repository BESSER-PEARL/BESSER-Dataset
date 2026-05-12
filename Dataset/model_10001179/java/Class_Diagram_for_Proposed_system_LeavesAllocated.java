





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_LeavesAllocated  {

    private String empId;
    private String leaveType;
    private String id;
    private String noOfLeaves;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;


    public Class_Diagram_for_Proposed_system_LeavesAllocated(
        String empId,        String leaveType,        String id,        String noOfLeaves    ) {
        this.empId = empId;
        this.leaveType = leaveType;
        this.id = id;
        this.noOfLeaves = noOfLeaves;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(String noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }

    public Class_Diagram_for_Proposed_system_Employee getClass_diagram_for_proposed_system_employee() {
        return class_diagram_for_proposed_system_employee;
    }

    public void setClass_diagram_for_proposed_system_employee(Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employee = class_diagram_for_proposed_system_employee;
    }

}