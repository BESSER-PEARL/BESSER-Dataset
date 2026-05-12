





import java.util.List;
import java.util.ArrayList;

public class PLACEMENTS_PAGE  {

    private int SALARY;
    private String BRANCH;
    private String INTREST;





    private WELCOME_PAGE welcome_page;


    public PLACEMENTS_PAGE(
        int SALARY,        String BRANCH,        String INTREST    ) {
        this.SALARY = SALARY;
        this.BRANCH = BRANCH;
        this.INTREST = INTREST;
    }


    public int getSalary() {
        return SALARY;
    }

    public void setSalary(int SALARY) {
        this.SALARY = SALARY;
    }
    public String getBranch() {
        return BRANCH;
    }

    public void setBranch(String BRANCH) {
        this.BRANCH = BRANCH;
    }
    public String getIntrest() {
        return INTREST;
    }

    public void setIntrest(String INTREST) {
        this.INTREST = INTREST;
    }

    public WELCOME_PAGE getWelcome_page() {
        return welcome_page;
    }

    public void setWelcome_page(WELCOME_PAGE welcome_page) {
        this.welcome_page = welcome_page;
    }

}