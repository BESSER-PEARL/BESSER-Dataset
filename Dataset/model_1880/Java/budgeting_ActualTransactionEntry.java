





import java.util.List;
import java.util.ArrayList;

public class budgeting_ActualTransactionEntry extends ActualEntry {






    private List<budgeting_Transaction> budgeting_transactions;


    public budgeting_ActualTransactionEntry(
    ) {
        super(
        );
        this.budgeting_transactions = new ArrayList<>();
    }

    public budgeting_ActualTransactionEntry(
        ArrayList<budgeting_Transaction> budgeting_transactions    ) {
        this.budgeting_transactions = budgeting_transactions;
    }


    public List<budgeting_Transaction> getBudgeting_transactions() {
        return budgeting_transactions;
    }

    public void addBudgeting_transaction(Budgeting_transaction budgeting_transaction) {
        this.budgeting_transactions.add(budgeting_transaction);
    }

}