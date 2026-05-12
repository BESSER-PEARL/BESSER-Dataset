





import java.util.List;
import java.util.ArrayList;

public class ETF_EPF  {

    private String rate;
    private String type;
    private int no;





    private Salary salary;


    public ETF_EPF(
        String rate,        String type,        int no    ) {
        this.rate = rate;
        this.type = type;
        this.no = no;
    }


    public String getRate() {
        return rate;
    }

    public void setRate(String rate) {
        this.rate = rate;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }

    public Salary getSalary() {
        return salary;
    }

    public void setSalary(Salary salary) {
        this.salary = salary;
    }

}