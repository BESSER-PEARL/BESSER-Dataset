





import java.util.List;
import java.util.ArrayList;

public class budgeting_Month  {

    private String name;





    private budgeting_Year budgeting_year;


    public budgeting_Month(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public budgeting_Year getBudgeting_year() {
        return budgeting_year;
    }

    public void setBudgeting_year(budgeting_Year budgeting_year) {
        this.budgeting_year = budgeting_year;
    }

}