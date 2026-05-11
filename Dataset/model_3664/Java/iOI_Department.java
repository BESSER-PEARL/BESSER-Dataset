





import java.util.List;
import java.util.ArrayList;

public class iOI_Department  {

    private String name;





    private List<iOI_Employee> ioi_employees;




    private iOI_Department ioi_department;




    private iOI_Company ioi_company;




    private iOI_Manager ioi_manager;


    public iOI_Department(
        String name    ) {
        this.name = name;
        this.ioi_employees = new ArrayList<>();
    }

    public iOI_Department(
        String name        ArrayList<iOI_Employee> ioi_employees    ) {
        this.name = name;
        this.ioi_employees = ioi_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<iOI_Employee> getIoi_employees() {
        return ioi_employees;
    }

    public void addIoi_employee(Ioi_employee ioi_employee) {
        this.ioi_employees.add(ioi_employee);
    }
    public iOI_Department getIoi_department() {
        return ioi_department;
    }

    public void setIoi_department(iOI_Department ioi_department) {
        this.ioi_department = ioi_department;
    }
    public iOI_Company getIoi_company() {
        return ioi_company;
    }

    public void setIoi_company(iOI_Company ioi_company) {
        this.ioi_company = ioi_company;
    }
    public iOI_Manager getIoi_manager() {
        return ioi_manager;
    }

    public void setIoi_manager(iOI_Manager ioi_manager) {
        this.ioi_manager = ioi_manager;
    }

}