





import java.util.List;
import java.util.ArrayList;

public class account_UserAccountController  {

    private None userAccountRepository;
    private String URL;





    private account_UserAccount account_useraccount;


    public account_UserAccountController(
        None userAccountRepository,        String URL    ) {
        this.userAccountRepository = userAccountRepository;
        this.URL = URL;
    }


    public None getUseraccountrepository() {
        return userAccountRepository;
    }

    public void setUseraccountrepository(None userAccountRepository) {
        this.userAccountRepository = userAccountRepository;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }

    public account_UserAccount getAccount_useraccount() {
        return account_useraccount;
    }

    public void setAccount_useraccount(account_UserAccount account_useraccount) {
        this.account_useraccount = account_useraccount;
    }

}