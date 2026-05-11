





import java.util.List;
import java.util.ArrayList;

public class office_Office extends OfficeElement {






    private office_Employee office_employee;




    private List<office_Employee> office_employees;


    public office_Office(
    ) {
        super(
        );
        this.office_employees = new ArrayList<>();
    }

    public office_Office(
        ArrayList<office_Employee> office_employees    ) {
        this.office_employees = office_employees;
    }


    public office_Employee getOffice_employee() {
        return office_employee;
    }

    public void setOffice_employee(office_Employee office_employee) {
        this.office_employee = office_employee;
    }
    public List<office_Employee> getOffice_employees() {
        return office_employees;
    }

    public void addOffice_employee(Office_employee office_employee) {
        this.office_employees.add(office_employee);
    }

}