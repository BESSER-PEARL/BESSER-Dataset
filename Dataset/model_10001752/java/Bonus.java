





import java.util.List;
import java.util.ArrayList;

public class Bonus  {

    private String amount;
    private int IDnum;
    private int id;
    private String type;





    private Salary salary;


    public Bonus(
        String amount,        int IDnum,        int id,        String type    ) {
        this.amount = amount;
        this.IDnum = IDnum;
        this.id = id;
        this.type = type;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getIdnum() {
        return IDnum;
    }

    public void setIdnum(int IDnum) {
        this.IDnum = IDnum;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Salary getSalary() {
        return salary;
    }

    public void setSalary(Salary salary) {
        this.salary = salary;
    }

}