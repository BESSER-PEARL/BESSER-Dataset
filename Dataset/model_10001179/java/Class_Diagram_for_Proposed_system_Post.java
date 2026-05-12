





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Post  {

    private String name;
    private String leavesEntitled;
    private String attribute;
    private String deptId;
    private String id;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;




    private Class_Diagram_for_Proposed_system_Department class_diagram_for_proposed_system_department;


    public Class_Diagram_for_Proposed_system_Post(
        String name,        String leavesEntitled,        String attribute,        String deptId,        String id    ) {
        this.name = name;
        this.leavesEntitled = leavesEntitled;
        this.attribute = attribute;
        this.deptId = deptId;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLeavesentitled() {
        return leavesEntitled;
    }

    public void setLeavesentitled(String leavesEntitled) {
        this.leavesEntitled = leavesEntitled;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getDeptid() {
        return deptId;
    }

    public void setDeptid(String deptId) {
        this.deptId = deptId;
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
    public Class_Diagram_for_Proposed_system_Department getClass_diagram_for_proposed_system_department() {
        return class_diagram_for_proposed_system_department;
    }

    public void setClass_diagram_for_proposed_system_department(Class_Diagram_for_Proposed_system_Department class_diagram_for_proposed_system_department) {
        this.class_diagram_for_proposed_system_department = class_diagram_for_proposed_system_department;
    }

}