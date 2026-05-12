





import java.util.List;
import java.util.ArrayList;

public class PLACEMENTS_PAGE  {

    private int SALARY;
    private String INTREST;
    private String BRANCH;



    public PLACEMENTS_PAGE(
        int SALARY,        String INTREST,        String BRANCH    ) {
        this.SALARY = SALARY;
        this.INTREST = INTREST;
        this.BRANCH = BRANCH;
    }


    public int getSalary() {
        return SALARY;
    }

    public void setSalary(int SALARY) {
        this.SALARY = SALARY;
    }
    public String getIntrest() {
        return INTREST;
    }

    public void setIntrest(String INTREST) {
        this.INTREST = INTREST;
    }
    public String getBranch() {
        return BRANCH;
    }

    public void setBranch(String BRANCH) {
        this.BRANCH = BRANCH;
    }


}