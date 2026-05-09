





import java.util.List;
import java.util.ArrayList;

public class budgeting_BudgetFactorEntry extends BudgetEntry {

    private float factor;





    private budgeting_BudgetEntry budgeting_budgetentry;


    public budgeting_BudgetFactorEntry(
        float factor    ) {
        super(
        );
        this.factor = factor;
    }


    public float getFactor() {
        return factor;
    }

    public void setFactor(float factor) {
        this.factor = factor;
    }

    public budgeting_BudgetEntry getBudgeting_budgetentry() {
        return budgeting_budgetentry;
    }

    public void setBudgeting_budgetentry(budgeting_BudgetEntry budgeting_budgetentry) {
        this.budgeting_budgetentry = budgeting_budgetentry;
    }

}