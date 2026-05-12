





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Department  {

    private String name;
    private String id;
    private String empId;





    private List<Class_Diagram_for_Proposed_system_Employee> class_diagram_for_proposed_system_employees;


    public Class_Diagram_for_Proposed_system_Department(
        String name,        String id,        String empId    ) {
        this.name = name;
        this.id = id;
        this.empId = empId;
        this.class_diagram_for_proposed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Proposed_system_Department(
        String name,        String id,        String empId        ArrayList<Class_Diagram_for_Proposed_system_Employee> class_diagram_for_proposed_system_employees    ) {
        this.name = name;
        this.id = id;
        this.empId = empId;
        this.class_diagram_for_proposed_system_employees = class_diagram_for_proposed_system_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEmpid() {
        return empId;
    }

    public void setEmpid(String empId) {
        this.empId = empId;
    }

    public List<Class_Diagram_for_Proposed_system_Employee> getClass_diagram_for_proposed_system_employees() {
        return class_diagram_for_proposed_system_employees;
    }

    public void addClass_diagram_for_proposed_system_employee(Class_diagram_for_proposed_system_employee class_diagram_for_proposed_system_employee) {
        this.class_diagram_for_proposed_system_employees.add(class_diagram_for_proposed_system_employee);
    }

}