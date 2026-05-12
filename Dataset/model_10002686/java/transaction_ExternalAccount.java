





import java.util.List;
import java.util.ArrayList;

public class transaction_ExternalAccount  {

    private String associatedAccount;
    private String routingNum;
    private String accountNum;



    public transaction_ExternalAccount(
        String associatedAccount,        String routingNum,        String accountNum    ) {
        this.associatedAccount = associatedAccount;
        this.routingNum = routingNum;
        this.accountNum = accountNum;
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


}