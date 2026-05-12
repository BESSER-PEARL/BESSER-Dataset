





import java.util.List;
import java.util.ArrayList;

public class ETF_EPF  {

    private int no;
    private String type;
    private String rate;





    private Salary salary;


    public ETF_EPF(
        int no,        String type,        String rate    ) {
        this.no = no;
        this.type = type;
        this.rate = rate;
    }


    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRate() {
        return rate;
    }

    public void setRate(String rate) {
        this.rate = rate;
    }

    public Salary getSalary() {
        return salary;
    }

    public void setSalary(Salary salary) {
        this.salary = salary;
    }

}