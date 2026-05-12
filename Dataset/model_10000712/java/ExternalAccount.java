





import java.util.List;
import java.util.ArrayList;

public class ExternalAccount  {

    private String routingNum;
    private String associatedAccount;
    private String accountNum;





    private Account2 account2;




    private List<TransferTransaction> transfertransactions;


    public ExternalAccount(
        String routingNum,        String associatedAccount,        String accountNum    ) {
        this.routingNum = routingNum;
        this.associatedAccount = associatedAccount;
        this.accountNum = accountNum;
        this.transfertransactions = new ArrayList<>();
    }

    public ExternalAccount(
        String routingNum,        String associatedAccount,        String accountNum        ArrayList<TransferTransaction> transfertransactions    ) {
        this.routingNum = routingNum;
        this.associatedAccount = associatedAccount;
        this.accountNum = accountNum;
        this.transfertransactions = transfertransactions;
    }

    public String getRoutingnum() {
        return routingNum;
    }

    public void setRoutingnum(String routingNum) {
        this.routingNum = routingNum;
    }
    public String getAssociatedaccount() {
        return associatedAccount;
    }

    public void setAssociatedaccount(String associatedAccount) {
        this.associatedAccount = associatedAccount;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }

    public Account2 getAccount2() {
        return account2;
    }

    public void setAccount2(Account2 account2) {
        this.account2 = account2;
    }
    public List<TransferTransaction> getTransfertransactions() {
        return transfertransactions;
    }

    public void addTransfertransaction(Transfertransaction transfertransaction) {
        this.transfertransactions.add(transfertransaction);
    }

}