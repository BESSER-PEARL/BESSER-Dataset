





import java.util.List;
import java.util.ArrayList;

public class transaction_ExternalAccount  {

    private String associatedAccount;
    private String routingNum;
    private String accountNum;





    private List<transaction_TransferTransaction> transaction_transfertransactions;


    public transaction_ExternalAccount(
        String associatedAccount,        String routingNum,        String accountNum    ) {
        this.associatedAccount = associatedAccount;
        this.routingNum = routingNum;
        this.accountNum = accountNum;
        this.transaction_transfertransactions = new ArrayList<>();
    }

    public transaction_ExternalAccount(
        String associatedAccount,        String routingNum,        String accountNum        ArrayList<transaction_TransferTransaction> transaction_transfertransactions    ) {
        this.associatedAccount = associatedAccount;
        this.routingNum = routingNum;
        this.accountNum = accountNum;
        this.transaction_transfertransactions = transaction_transfertransactions;
    }

    public String getAssociatedaccount() {
        return associatedAccount;
    }

    public void setAssociatedaccount(String associatedAccount) {
        this.associatedAccount = associatedAccount;
    }
    public String getRoutingnum() {
        return routingNum;
    }

    public void setRoutingnum(String routingNum) {
        this.routingNum = routingNum;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }

    public List<transaction_TransferTransaction> getTransaction_transfertransactions() {
        return transaction_transfertransactions;
    }

    public void addTransaction_transfertransaction(Transaction_transfertransaction transaction_transfertransaction) {
        this.transaction_transfertransactions.add(transaction_transfertransaction);
    }

}