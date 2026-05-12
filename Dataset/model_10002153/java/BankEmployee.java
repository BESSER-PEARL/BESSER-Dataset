





import java.util.List;
import java.util.ArrayList;

public class BankEmployee  {

    private int EmployeeID;
    private String Name;
    private int Salary;
    private String EmpAdd;





    private Bank bank;


    public BankEmployee(
        int EmployeeID,        String Name,        int Salary,        String EmpAdd    ) {
        this.EmployeeID = EmployeeID;
        this.Name = Name;
        this.Salary = Salary;
        this.EmpAdd = EmpAdd;
    }


    public int getEmployeeid() {
        return EmployeeID;
    }

    public void setEmployeeid(int EmployeeID) {
        this.EmployeeID = EmployeeID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }
    public String getEmpadd() {
        return EmpAdd;
    }

    public void setEmpadd(String EmpAdd) {
        this.EmpAdd = EmpAdd;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}