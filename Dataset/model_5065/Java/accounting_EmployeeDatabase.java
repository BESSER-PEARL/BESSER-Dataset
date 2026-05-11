





import java.util.List;
import java.util.ArrayList;

public class accounting_EmployeeDatabase  {






    private List<accounting_Employee> accounting_employees;


    public accounting_EmployeeDatabase(
    ) {
        this.accounting_employees = new ArrayList<>();
    }

    public accounting_EmployeeDatabase(
        ArrayList<accounting_Employee> accounting_employees    ) {
        this.accounting_employees = accounting_employees;
    }


    public List<accounting_Employee> getAccounting_employees() {
        return accounting_employees;
    }

    public void addAccounting_employee(Accounting_employee accounting_employee) {
        this.accounting_employees.add(accounting_employee);
    }

}