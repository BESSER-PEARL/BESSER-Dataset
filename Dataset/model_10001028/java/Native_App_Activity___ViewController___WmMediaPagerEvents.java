





import java.util.List;
import java.util.ArrayList;

public class Native_App_Activity___ViewController___WmMediaPagerEvents  {

    private float balance;
    private String accountNo;
    private None type;





    private List<WmMediaPager_Mini_App_WmMediaPager> wmmediapager_mini_app_wmmediapagers;


    public Native_App_Activity___ViewController___WmMediaPagerEvents(
        float balance,        String accountNo,        None type    ) {
        this.balance = balance;
        this.accountNo = accountNo;
        this.type = type;
        this.wmmediapager_mini_app_wmmediapagers = new ArrayList<>();
    }

    public Native_App_Activity___ViewController___WmMediaPagerEvents(
        float balance,        String accountNo,        None type        ArrayList<WmMediaPager_Mini_App_WmMediaPager> wmmediapager_mini_app_wmmediapagers    ) {
        this.balance = balance;
        this.accountNo = accountNo;
        this.type = type;
        this.wmmediapager_mini_app_wmmediapagers = wmmediapager_mini_app_wmmediapagers;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }

    public List<WmMediaPager_Mini_App_WmMediaPager> getWmmediapager_mini_app_wmmediapagers() {
        return wmmediapager_mini_app_wmmediapagers;
    }

    public void addWmmediapager_mini_app_wmmediapager(Wmmediapager_mini_app_wmmediapager wmmediapager_mini_app_wmmediapager) {
        this.wmmediapager_mini_app_wmmediapagers.add(wmmediapager_mini_app_wmmediapager);
    }

}