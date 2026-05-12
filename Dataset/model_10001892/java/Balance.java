





import java.util.List;
import java.util.ArrayList;

public class Balance  {

    private int tokens;





    private Account account;


    public Balance(
        int tokens    ) {
        this.tokens = tokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}