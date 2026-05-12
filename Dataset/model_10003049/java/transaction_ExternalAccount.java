





import java.util.List;
import java.util.ArrayList;

public class transaction_ExternalAccount  {

    private String accountNum;
    private String routingNum;
    private String associatedAccount;



    public transaction_ExternalAccount(
        String accountNum,        String routingNum,        String associatedAccount    ) {
        this.accountNum = accountNum;
        this.routingNum = routingNum;
        this.associatedAccount = associatedAccount;
    }


    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
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


}