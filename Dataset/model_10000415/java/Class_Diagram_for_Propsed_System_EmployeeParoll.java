





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EmployeeParoll  {

    private String lateamount;
    private int empid;
    private String otamount;
    private String dotamount;
    private String basicslaray;
    private String etf;
    private int id;
    private String epf;





    private List<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees;


    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        String lateamount,        int empid,        String otamount,        String dotamount,        String basicslaray,        String etf,        int id,        String epf    ) {
        this.lateamount = lateamount;
        this.empid = empid;
        this.otamount = otamount;
        this.dotamount = dotamount;
        this.basicslaray = basicslaray;
        this.etf = etf;
        this.id = id;
        this.epf = epf;
        this.class_diagram_for_propsed_system_employees = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_EmployeeParoll(
        String lateamount,        int empid,        String otamount,        String dotamount,        String basicslaray,        String etf,        int id,        String epf        ArrayList<Class_Diagram_for_Propsed_System_Employee> class_diagram_for_propsed_system_employees    ) {
        this.lateamount = lateamount;
        this.empid = empid;
        this.otamount = otamount;
        this.dotamount = dotamount;
        this.basicslaray = basicslaray;
        this.etf = etf;
        this.id = id;
        this.epf = epf;
        this.class_diagram_for_propsed_system_employees = class_diagram_for_propsed_system_employees;
    }

    public String getLateamount() {
        return lateamount;
    }

    public void setLateamount(String lateamount) {
        this.lateamount = lateamount;
    }
    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public String getOtamount() {
        return otamount;
    }

    public void setOtamount(String otamount) {
        this.otamount = otamount;
    }
    public String getDotamount() {
        return dotamount;
    }

    public void setDotamount(String dotamount) {
        this.dotamount = dotamount;
    }
    public String getBasicslaray() {
        return basicslaray;
    }

    public void setBasicslaray(String basicslaray) {
        this.basicslaray = basicslaray;
    }
    public String getEtf() {
        return etf;
    }

    public void setEtf(String etf) {
        this.etf = etf;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEpf() {
        return epf;
    }

    public void setEpf(String epf) {
        this.epf = epf;
    }

    public List<Class_Diagram_for_Propsed_System_Employee> getClass_diagram_for_propsed_system_employees() {
        return class_diagram_for_propsed_system_employees;
    }

    public void addClass_diagram_for_propsed_system_employee(Class_diagram_for_propsed_system_employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employees.add(class_diagram_for_propsed_system_employee);
    }

}