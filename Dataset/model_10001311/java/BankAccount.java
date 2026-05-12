





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private int TRANSACTION_FEE;
    private float minimumBalance;
    private float balance;
    private int numOfTransactions;
    private int FREE_TRANSACTIONS;
    private boolean isActive;



    public BankAccount(
        int TRANSACTION_FEE,        float minimumBalance,        float balance,        int numOfTransactions,        int FREE_TRANSACTIONS,        boolean isActive    ) {
        this.TRANSACTION_FEE = TRANSACTION_FEE;
        this.minimumBalance = minimumBalance;
        this.balance = balance;
        this.numOfTransactions = numOfTransactions;
        this.FREE_TRANSACTIONS = FREE_TRANSACTIONS;
        this.isActive = isActive;
    }


    public int getTransaction_fee() {
        return TRANSACTION_FEE;
    }

    public void setTransaction_fee(int TRANSACTION_FEE) {
        this.TRANSACTION_FEE = TRANSACTION_FEE;
    }
    public float getMinimumbalance() {
        return minimumBalance;
    }

    public void setMinimumbalance(float minimumBalance) {
        this.minimumBalance = minimumBalance;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public int getNumoftransactions() {
        return numOfTransactions;
    }

    public void setNumoftransactions(int numOfTransactions) {
        this.numOfTransactions = numOfTransactions;
    }
    public int getFree_transactions() {
        return FREE_TRANSACTIONS;
    }

    public void setFree_transactions(int FREE_TRANSACTIONS) {
        this.FREE_TRANSACTIONS = FREE_TRANSACTIONS;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }


}