





import java.util.List;
import java.util.ArrayList;

public class employee_Employee extends NamedEntity {

    private int wage;





    private employee_Department employee_department;


    public employee_Employee(
        int wage    ) {
        super(
        );
        this.wage = wage;
    }


    public int getWage() {
        return wage;
    }

    public void setWage(int wage) {
        this.wage = wage;
    }

    public employee_Department getEmployee_department() {
        return employee_department;
    }

    public void setEmployee_department(employee_Department employee_department) {
        this.employee_department = employee_department;
    }

}