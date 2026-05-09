





import java.util.List;
import java.util.ArrayList;

public class budgeting_BudgetAmountEntry extends BudgetEntry {

    private String amount;



    public budgeting_BudgetAmountEntry(
        String amount    ) {
        super(
        );
        this.amount = amount;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }


}