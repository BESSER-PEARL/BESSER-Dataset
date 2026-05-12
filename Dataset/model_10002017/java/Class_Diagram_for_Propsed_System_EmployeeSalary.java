





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EmployeeSalary  {

    private boolean deductions;
    private String emp_id;
    private String id;
    private boolean allowances;
    private String basic_salary;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_EmployeeSalary(
        boolean deductions,        String emp_id,        String id,        boolean allowances,        String basic_salary    ) {
        this.deductions = deductions;
        this.emp_id = emp_id;
        this.id = id;
        this.allowances = allowances;
        this.basic_salary = basic_salary;
    }


    public boolean getDeductions() {
        return deductions;
    }

    public void setDeductions(boolean deductions) {
        this.deductions = deductions;
    }
    public String getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(String emp_id) {
        this.emp_id = emp_id;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getAllowances() {
        return allowances;
    }

    public void setAllowances(boolean allowances) {
        this.allowances = allowances;
    }
    public String getBasic_salary() {
        return basic_salary;
    }

    public void setBasic_salary(String basic_salary) {
        this.basic_salary = basic_salary;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}