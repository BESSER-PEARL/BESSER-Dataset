





import java.util.List;
import java.util.ArrayList;

public class RandL_TransactionReport  {

    private String totalBurned;
    private String balance;
    private String totalEarned;
    private String number;
    private String name;





    private RandL_Date randl_date;




    private RandL_CustomerCard randl_customercard;




    private RandL_Date randl_date;


    public RandL_TransactionReport(
        String totalBurned,        String balance,        String totalEarned,        String number,        String name    ) {
        this.totalBurned = totalBurned;
        this.balance = balance;
        this.totalEarned = totalEarned;
        this.number = number;
        this.name = name;
    }


    public String getTotalburned() {
        return totalBurned;
    }

    public void setTotalburned(String totalBurned) {
        this.totalBurned = totalBurned;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }
    public String getTotalearned() {
        return totalEarned;
    }

    public void setTotalearned(String totalEarned) {
        this.totalEarned = totalEarned;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public RandL_CustomerCard getRandl_customercard() {
        return randl_customercard;
    }

    public void setRandl_customercard(RandL_CustomerCard randl_customercard) {
        this.randl_customercard = randl_customercard;
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }

}