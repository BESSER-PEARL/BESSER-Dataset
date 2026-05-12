





import java.util.List;
import java.util.ArrayList;

public class Bonus  {

    private int IDnum;
    private int id;
    private String type;
    private String amount;





    private Salary salary;


    public Bonus(
        int IDnum,        int id,        String type,        String amount    ) {
        this.IDnum = IDnum;
        this.id = id;
        this.type = type;
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
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public Salary getSalary() {
        return salary;
    }

    public void setSalary(Salary salary) {
        this.salary = salary;
    }

}