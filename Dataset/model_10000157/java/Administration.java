





import java.util.List;
import java.util.ArrayList;

public class Administration  {

    private None Office_Manager;
    private None CFO;
    private None Executive_Director___COO;
    private None Asst__Executive_Director;





    private Employee_DB employee_db;


    public Administration(
        None Office_Manager,        None CFO,        None Executive_Director___COO,        None Asst__Executive_Director    ) {
        this.Office_Manager = Office_Manager;
        this.CFO = CFO;
        this.Executive_Director___COO = Executive_Director___COO;
        this.Asst__Executive_Director = Asst__Executive_Director;
    }


    public None getOffice_manager() {
        return Office_Manager;
    }

    public void setOffice_manager(None Office_Manager) {
        this.Office_Manager = Office_Manager;
    }
    public None getCfo() {
        return CFO;
    }

    public void setCfo(None CFO) {
        this.CFO = CFO;
    }
    public None getExecutive_director___coo() {
        return Executive_Director___COO;
    }

    public void setExecutive_director___coo(None Executive_Director___COO) {
        this.Executive_Director___COO = Executive_Director___COO;
    }
    public None getAsst__executive_director() {
        return Asst__Executive_Director;
    }

    public void setAsst__executive_director(None Asst__Executive_Director) {
        this.Asst__Executive_Director = Asst__Executive_Director;
    }

    public Employee_DB getEmployee_db() {
        return employee_db;
    }

    public void setEmployee_db(Employee_DB employee_db) {
        this.employee_db = employee_db;
    }

}