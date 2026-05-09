





import java.util.List;
import java.util.ArrayList;

public class budgeting_Year extends BudgetingFile {

    private int name;





    private budgeting_Library budgeting_library;


    public budgeting_Year(
        int name    ) {
        super(
        );
        this.name = name;
    }


    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }

    public budgeting_Library getBudgeting_library() {
        return budgeting_library;
    }

    public void setBudgeting_library(budgeting_Library budgeting_library) {
        this.budgeting_library = budgeting_library;
    }

}