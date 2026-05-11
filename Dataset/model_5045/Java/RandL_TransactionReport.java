





import java.util.List;
import java.util.ArrayList;

public class RandL_TransactionReport  {

    private String name;
    private String number;
    private String totalBurned;
    private String totalEarned;
    private String balance;





    private RandL_Date randl_date;




    private RandL_Date randl_date;


    public RandL_TransactionReport(
        String name,        String number,        String totalBurned,        String totalEarned,        String balance    ) {
        this.name = name;
        this.number = number;
        this.totalBurned = totalBurned;
        this.totalEarned = totalEarned;
        this.balance = balance;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getTotalburned() {
        return totalBurned;
    }

    public void setTotalburned(String totalBurned) {
        this.totalBurned = totalBurned;
    }
    public String getTotalearned() {
        return totalEarned;
    }

    public void setTotalearned(String totalEarned) {
        this.totalEarned = totalEarned;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }

    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }

}