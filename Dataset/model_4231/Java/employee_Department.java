





import java.util.List;
import java.util.ArrayList;

public class employee_Department extends NamedEntity {

    private boolean isRich;





    private employee_Company employee_company;


    public employee_Department(
        boolean isRich    ) {
        super(
        );
        this.isRich = isRich;
    }


    public boolean getIsrich() {
        return isRich;
    }

    public void setIsrich(boolean isRich) {
        this.isRich = isRich;
    }

    public employee_Company getEmployee_company() {
        return employee_company;
    }

    public void setEmployee_company(employee_Company employee_company) {
        this.employee_company = employee_company;
    }

}