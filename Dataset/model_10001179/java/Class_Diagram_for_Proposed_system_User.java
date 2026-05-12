





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_User  {

    private int roleId;
    private String LastName;
    private String id;
    private String firstNAme;





    private Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee;


    public Class_Diagram_for_Proposed_system_User(
        int roleId,        String LastName,        String id,        String firstNAme    ) {
        this.roleId = roleId;
        this.LastName = LastName;
        this.id = id;
        this.firstNAme = firstNAme;
    }


    public int getRoleid() {
        return roleId;
    }

    public void setRoleid(int roleId) {
        this.roleId = roleId;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFirstname() {
        return firstNAme;
    }

    public void setFirstname(String firstNAme) {
        this.firstNAme = firstNAme;
    }

    public Class_Diagram_for_Proposed_system_Employee getClass_diagram_for_proposed_system_employee() {
        return class_diagram_for_proposed_system_employee;
    }

    public void setClass_diagram_for_proposed_system_employee(Class_Diagram_for_Proposed_system_Employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employee = class_diagram_for_proposed_system_employee;
    }

}