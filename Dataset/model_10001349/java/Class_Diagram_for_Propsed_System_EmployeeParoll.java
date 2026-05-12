





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EmployeeParoll  {

    private int otamount;
    private int empid;
    private int doyamount;
    private int empid3;
    private int basicslaray;
    private int id;
    private int epf;
    private String etf;





    private List<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees;


    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        int otamount,        int empid,        int doyamount,        int empid3,        int basicslaray,        int id,        int epf,        String etf    ) {
        this.otamount = otamount;
        this.empid = empid;
        this.doyamount = doyamount;
        this.empid3 = empid3;
        this.basicslaray = basicslaray;
        this.id = id;
        this.epf = epf;
        this.etf = etf;
        this.class_diagram_for_propsed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        int otamount,        int empid,        int doyamount,        int empid3,        int basicslaray,        int id,        int epf,        String etf        ArrayList<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees    ) {
        this.otamount = otamount;
        this.empid = empid;
        this.doyamount = doyamount;
        this.empid3 = empid3;
        this.basicslaray = basicslaray;
        this.id = id;
        this.epf = epf;
        this.etf = etf;
        this.class_diagram_for_propsed_system_employees = class_diagram_for_propsed_system_employees;
    }

    public int getOtamount() {
        return otamount;
    }

    public void setOtamount(int otamount) {
        this.otamount = otamount;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public int getDoyamount() {
        return doyamount;
    }

    public void setDoyamount(int doyamount) {
        this.doyamount = doyamount;
    }
    public int getEmpid3() {
        return empid3;
    }

    public void setEmpid3(int empid3) {
        this.empid3 = empid3;
    }
    public int getBasicslaray() {
        return basicslaray;
    }

    public void setBasicslaray(int basicslaray) {
        this.basicslaray = basicslaray;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getEpf() {
        return epf;
    }

    public void setEpf(int epf) {
        this.epf = epf;
    }
    public String getEtf() {
        return etf;
    }

    public void setEtf(String etf) {
        this.etf = etf;
    }

    public List<Class_Diagram_for_Propsed_System_Employee> getClass_diagram_for_propsed_system_employees() {
        return class_diagram_for_propsed_system_employees;
    }

    public void addClass_diagram_for_propsed_system_employee(Class_diagram_for_propsed_system_employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employees.add(class_diagram_for_propsed_system_employee);
    }

}