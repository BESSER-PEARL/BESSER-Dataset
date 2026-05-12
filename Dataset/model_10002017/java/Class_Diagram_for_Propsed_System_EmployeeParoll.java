





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EmployeeParoll  {

    private int id;
    private String lateamount;
    private String dotamount;
    private String epf;
    private String otamount;
    private String basicslaray;
    private int empid;
    private String etf;





    private List<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees;


    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        int id,        String lateamount,        String dotamount,        String epf,        String otamount,        String basicslaray,        int empid,        String etf    ) {
        this.id = id;
        this.lateamount = lateamount;
        this.dotamount = dotamount;
        this.epf = epf;
        this.otamount = otamount;
        this.basicslaray = basicslaray;
        this.empid = empid;
        this.etf = etf;
        this.class_diagram_for_propsed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        int id,        String lateamount,        String dotamount,        String epf,        String otamount,        String basicslaray,        int empid,        String etf        ArrayList<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees    ) {
        this.id = id;
        this.lateamount = lateamount;
        this.dotamount = dotamount;
        this.epf = epf;
        this.otamount = otamount;
        this.basicslaray = basicslaray;
        this.empid = empid;
        this.etf = etf;
        this.class_diagram_for_propsed_system_employees = class_diagram_for_propsed_system_employees;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLateamount() {
        return lateamount;
    }

    public void setLateamount(String lateamount) {
        this.lateamount = lateamount;
    }
    public String getDotamount() {
        return dotamount;
    }

    public void setDotamount(String dotamount) {
        this.dotamount = dotamount;
    }
    public String getEpf() {
        return epf;
    }

    public void setEpf(String epf) {
        this.epf = epf;
    }
    public String getOtamount() {
        return otamount;
    }

    public void setOtamount(String otamount) {
        this.otamount = otamount;
    }
    public String getBasicslaray() {
        return basicslaray;
    }

    public void setBasicslaray(String basicslaray) {
        this.basicslaray = basicslaray;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
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