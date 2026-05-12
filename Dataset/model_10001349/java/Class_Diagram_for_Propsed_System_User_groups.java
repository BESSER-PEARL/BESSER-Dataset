





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_User_groups  {

    private String attribute2;
    private String attribute3;
    private String attribute;





    private List<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees;


    public Class_Diagram_for_Propsed_System_User_groups(
        String attribute2,        String attribute3,        String attribute    ) {
        this.attribute2 = attribute2;
        this.attribute3 = attribute3;
        this.attribute = attribute;
        this.class_diagram_for_propsed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_User_groups(
        String attribute2,        String attribute3,        String attribute        ArrayList<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees    ) {
        this.attribute2 = attribute2;
        this.attribute3 = attribute3;
        this.attribute = attribute;
        this.class_diagram_for_propsed_system_employees = class_diagram_for_propsed_system_employees;
    }

    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public List<Class_Diagram_for_Propsed_System_Employee> getClass_diagram_for_propsed_system_employees() {
        return class_diagram_for_propsed_system_employees;
    }

    public void addClass_diagram_for_propsed_system_employee(Class_diagram_for_propsed_system_employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employees.add(class_diagram_for_propsed_system_employee);
    }

}