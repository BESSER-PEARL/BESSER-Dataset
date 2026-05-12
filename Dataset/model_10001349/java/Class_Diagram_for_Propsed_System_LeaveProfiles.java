





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_LeaveProfiles  {

    private String name;
    private int anual;
    private int casual;
    private int id;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_LeaveProfiles(
        String name,        int anual,        int casual,        int id    ) {
        this.name = name;
        this.anual = anual;
        this.casual = casual;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAnual() {
        return anual;
    }

    public void setAnual(int anual) {
        this.anual = anual;
    }
    public int getCasual() {
        return casual;
    }

    public void setCasual(int casual) {
        this.casual = casual;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}