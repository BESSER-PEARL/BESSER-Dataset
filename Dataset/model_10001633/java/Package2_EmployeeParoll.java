





import java.util.List;
import java.util.ArrayList;

public class Package2_EmployeeParoll  {

    private int epf;
    private String etf;
    private int otamount;
    private int empid;
    private int id;
    private int doyamount;
    private int basicslaray;
    private int empid3;





    private List<Package2_Employee> package2_employees;


    public Package2_EmployeeParoll(
        int epf,        String etf,        int otamount,        int empid,        int id,        int doyamount,        int basicslaray,        int empid3    ) {
        this.epf = epf;
        this.etf = etf;
        this.otamount = otamount;
        this.empid = empid;
        this.id = id;
        this.doyamount = doyamount;
        this.basicslaray = basicslaray;
        this.empid3 = empid3;
        this.package2_employees = new ArrayList<>();
    }

    public Package2_EmployeeParoll(
        int epf,        String etf,        int otamount,        int empid,        int id,        int doyamount,        int basicslaray,        int empid3        ArrayList<Package2_Employee> package2_employees    ) {
        this.epf = epf;
        this.etf = etf;
        this.otamount = otamount;
        this.empid = empid;
        this.id = id;
        this.doyamount = doyamount;
        this.basicslaray = basicslaray;
        this.empid3 = empid3;
        this.package2_employees = package2_employees;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDoyamount() {
        return doyamount;
    }

    public void setDoyamount(int doyamount) {
        this.doyamount = doyamount;
    }
    public int getBasicslaray() {
        return basicslaray;
    }

    public void setBasicslaray(int basicslaray) {
        this.basicslaray = basicslaray;
    }
    public int getEmpid3() {
        return empid3;
    }

    public void setEmpid3(int empid3) {
        this.empid3 = empid3;
    }

    public List<Package2_Employee> getPackage2_employees() {
        return package2_employees;
    }

    public void addPackage2_employee(Package2_employee package2_employee) {
        this.package2_employees.add(package2_employee);
    }

}