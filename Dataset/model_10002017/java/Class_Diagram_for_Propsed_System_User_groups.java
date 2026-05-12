





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_User_groups  {

    private String user_group;
    private int id;





    private List<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees;


    public Class_Diagram_for_Propsed_System_User_groups(
        String user_group,        int id    ) {
        this.user_group = user_group;
        this.id = id;
        this.class_diagram_for_propsed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_User_groups(
        String user_group,        int id        ArrayList<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees    ) {
        this.user_group = user_group;
        this.id = id;
        this.class_diagram_for_propsed_system_employees = class_diagram_for_propsed_system_employees;
    }

    public String getUser_group() {
        return user_group;
    }

    public void setUser_group(String user_group) {
        this.user_group = user_group;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Class_Diagram_for_Propsed_System_Employee> getClass_diagram_for_propsed_system_employees() {
        return class_diagram_for_propsed_system_employees;
    }

    public void addClass_diagram_for_propsed_system_employee(Class_diagram_for_propsed_system_employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employees.add(class_diagram_for_propsed_system_employee);
    }

}