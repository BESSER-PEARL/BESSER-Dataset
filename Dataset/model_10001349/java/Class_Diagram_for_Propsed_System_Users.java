





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Users  {

    private int lastname;
    private int firstname;
    private int password;
    private int id;
    private int email;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Users(
        int lastname,        int firstname,        int password,        int id,        int email    ) {
        this.lastname = lastname;
        this.firstname = firstname;
        this.password = password;
        this.id = id;
        this.email = email;
    }


    public int getLastname() {
        return lastname;
    }

    public void setLastname(int lastname) {
        this.lastname = lastname;
    }
    public int getFirstname() {
        return firstname;
    }

    public void setFirstname(int firstname) {
        this.firstname = firstname;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getEmail() {
        return email;
    }

    public void setEmail(int email) {
        this.email = email;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}