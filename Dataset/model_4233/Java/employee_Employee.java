





import java.util.List;
import java.util.ArrayList;

public class employee_Employee extends NamedEntity {

    private int wage;



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


}